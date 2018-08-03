import json
import os
import shutil
import urllib.request
from xml.etree import ElementTree as ET

from dicttoxml import dicttoxml
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .vacants import get_vacants
from .jobs import all_jobs, analyse_file
from random import randrange, uniform
cv_summary = {}


def home(request):
    return render(request, 'formuploads/index.html')


def show_json(request):
    if 'cv_summary' in request.session:
        cv = request.session['cv_summary']
    return HttpResponse(json.dumps(cv, ensure_ascii=False), content_type="application/json")


def show_xml(request):
    if 'cv_summary' in request.session:
        cv = request.session['cv_summary']
    return HttpResponse(dicttoxml(cv, custom_root='cv_summary', attr_type=False), content_type="application/xml")


@csrf_exempt
def upload(request):

    all_vacants_info = [{}]
    vacants_ids = []
    vacants_ids, cv_summary = handle_uploaded_file(
        request.FILES['file'], str(request.FILES['file']))
    request.session['cv_summary'] = cv_summary
    all_vacants_info = analyse_file(all_vacants_info, vacants_ids)

    if request.method == 'POST':
        recommend = [str()]
        recommend.pop(0)
        for key in cv_summary:
            if (len(cv_summary[key]) < 5 and key != 'other'):
                recommend.append("У вас слишком мало информации в категории: " +
                                 str(key) + " добавьте больше информации")
        recommend_len = len(recommend)
        return render(request, 'formuploads/success.html', {'vacants': all_vacants_info,
                                                            'cv_summary': cv_summary, 'recommend': recommend, 'recommend_len': recommend_len})
    return render(request, 'formuploads/failed.html', {'error': 'Невозможно загрузить резюме'})


def test(request):
    if 'cv_summary' in request.session:
        cv = request.session['cv_summary']
    for k in cv:
        for v in cv[k]:
            if "C++" in v or "c++" in v:
                return render(request, 'formuploads/test.html')
    return render(request, 'formuploads/failed.html', {'error': 'Нет подходящего теста для вас'})


def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    dir_path = 'upload/' + filename
    results = []
    results, cv_summary = get_vacants(dir_path)
    if os.path.exists('upload/'):
        shutil.rmtree('upload/')
    return results, cv_summary

def search(search_type="job_name",search_for="" ):
    all_jobs_array=all_jobs()
    found_job=[{}]
    
    
    for value in all_jobs_array[search_type]:      
        if search_for in value:
            found_job.append({search_type:value})
            return found_job
    return None                
                    
def search_v(request):
    if(request.GET.get('search_btn')):
        found_job=search(request.GET.get('search_text'))

    return render(request,'formuploads/search.html', {'found_job':found_job})


def rate(request):
    if 'cv_summary' in request.session:
        cv = request.session['cv_summary']
    cnt = 0
    if len(cv['skills']) >= 5:
        cnt += uniform(18,20)
    elif len(cv['skills']) > 0:
        cnt += 5
    if len(cv['education']) >= 5:
        cnt += uniform(18,20)
    elif len(cv['education']) > 0:
        cnt += 5
    if len(cv['experience']) >= 5:
        cnt += uniform(18,20)
    elif len(cv['experience']) > 0:
        cnt += 5    
    if len(cv['language']) >= 2:
        cnt += uniform(8,10)
    elif len(cv['language']) > 0:
        cnt += 5
    if len(cv['position']) >= 5:
        cnt += uniform(8,10)
    elif len(cv['position']) > 0:
        cnt += 5
    if len(cv['about']) > 0:
        cnt += 5
    if len(cv['reference']) > 0:
        cnt += 5
    cnt += uniform(-3,3)
    if cnt > 100:
        cnt = 100
    if cnt < 0:
        cnt = 0
    return render(request, 'formuploads/rate.html',{"percentage": int(cnt)})