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
            if (len(cv_summary[key]) < 5):
                recommend.append("У вас слишком мало информации в категории: " +
                                 str(key) + " добавьте больше информации")
        recommend_len = len(recommend)
        return render(request, 'formuploads/success.html', {'vacants': all_vacants_info,
                                                            'cv_summary': cv_summary, 'recommend': recommend, 'recommend_len': recommend_len})
    return render(request, 'formuploads/failed.html')


def test(request):
    return render(request, 'formuploads/test.html')


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

def search(search_type="job_name",search_text="программист 1с"):
    all_jobs_array=all_jobs()
    
    found_job=[{}]
    
    for value in all_jobs_array:
        for key in value:
            if key == search_type and search_text in value[key]:
                found_job.append(value)
                    


    return found_job                 
                    
def search_v(request):
    job_name, job_region, job_description = False, False, False
    name="job_name"
    job_name=request.GET.get('job_name')
    job_region  =request.GET.get('job_region')
    job_description=request.GET.get('job_description')

    search_txt = request.GET['search_text']
    if job_name=='True':
        name="job_name"
    if job_region=='True':
        name="job_region"
    if job_description=='True':
        name="job_description"

    found_job=search(name,search_txt)
    #found_job=search("job_name",search_txt)
    
    print(search_txt)
    return render(request,'formuploads/search.html', {'found_job':found_job, 'check':[job_name,job_region,job_description] , 'name':name})


    


        