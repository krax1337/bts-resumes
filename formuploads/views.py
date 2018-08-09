import json
import pdfkit
import os
import shutil
import urllib.request
from django.conf import settings
from xml.etree import ElementTree as ET
from wsgiref.util import FileWrapper

from dicttoxml import dicttoxml
from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse
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
	try:
		vacants_ids, cv_summary = handle_uploaded_file(
			request.FILES['file'], str(request.FILES['file']))
	except:
		return render(request, 'formuploads/failed.html', {'error': 'Поддерживаемые форматы: pdf, doc, docx, rtf'})
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

def search(search_type="job_name",search_text="программист 1с"):
	all_jobs_array=all_jobs()
	
	found_job=[{}]
	
	for value in all_jobs_array:
		for key in value:
			if key == search_type and search_text.lower() in value[key].lower():
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
	
	
	return render(request,'formuploads/search.html', {'found_job':found_job, 'check':[job_name,job_region,job_description] , 'name':name})

def generate_pdf(request):
	
	return render(request,'formuploads/generate_pdf.html')

def resume_create(request):
	resume = {}
	resume['firstname'] = request.GET.get('firstname')
	resume['lastname'] = request.GET.get('lastname')
	resume['phone'] = request.GET.get('phone')
	resume['email'] = request.GET.get('email')
	resume['address'] = request.GET.get('address')
	resume['positions'] = request.GET.get('positions')
	resume['skills'] = request.GET.get('skills')
	resume['about'] = request.GET.get('about')
	resume['educations'] = [{}]
	resume['experiences'] = [{}]

	counter_1 = 0
	try:
		counter_1_stp = int(request.GET.get('counter_1'))
	except:
		counter_1_stp = 0

	if(counter_1_stp == '0' or None):
		counter_1_stp = 0

	while True:
		counter_1 += 1
		if(counter_1 > counter_1_stp):
			break
		resume['educations'].append({
			'name': request.GET.get('education_name' + str(counter_1)),
			'degree': request.GET.get('education_degree' + str(counter_1)),
			'start_date': request.GET.get('education_start_date' + str(counter_1)),
			'end_date': request.GET.get('education_end_date' + str(counter_1)),
			'description': request.GET.get('education_description' + str(counter_1)),
		})
	resume['educations'].pop(0)



	counter_2 = 0
	try:
		counter_2_stp = int(request.GET.get('counter_2'))
	except:
		counter_2_stp = 0

	if(counter_2_stp == '0' or None):
		counter_2_stp = 0

	while True:
		counter_2 += 1
		if(counter_2 > counter_2_stp):
			break
		resume['experiences'].append({
			'name': request.GET.get('experience_name' + str(counter_2)),
			'degree': request.GET.get('experience_designation' + str(counter_2)),
			'start_date': request.GET.get('experience_start_date' + str(counter_2)),
			'end_date': request.GET.get('experience_end_date' + str(counter_2)),
			'description': request.GET.get('experience_description' + str(counter_2)),
		})
	resume['experiences'].pop(0)



	# resume['languages'] = request.GET.get('about')
	print(resume)
	return render(request, 'formuploads/resume_create.html',{'resume': resume})

def extract_pdf(request):
	# if not os.path.exists('pdf_resumes/'):
	# 	os.mkdir('pdf_resumes/')
		
	
	# f = open("резюме.pdf","w+")
	path_wkthmltopdf = r'C:\Python27\wkhtmltopdf\bin\wkhtmltopdf.exe'
	config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
	
	pdfkit.from_url('http://localhost:8000/generate_pdf/resume_create/resume/', "download/резюме.pdf",configuration=config)
	# f.write(pdf)
	#shutil.rmtree('')

def download_pdf(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
def rate(request):
	if 'cv_summary' in request.session:
		cv = request.session['cv_summary']
		cv.pop("other")
	cnt = 0
	recommendations = []
	if len(cv['skills']) >= 5:
		cnt += randrange(18,20)
	elif len(cv['skills']) > 0:
		cnt += 10
		recommendations.append('skills')
	else:
		recommendations.append('skills')
	if len(cv['education']) >= 5:
		cnt += randrange(18,20)
	elif len(cv['education']) > 0:
		cnt += 10
		recommendations.append('education')
	else:
		recommendations.append('education')
	if len(cv['experience']) >= 5:
		cnt += randrange(18,20)
	elif len(cv['experience']) > 0:
		cnt += 10    
		recommendations.append('experience')
	else:
		recommendations.append('experience')
	if len(cv['language']) >= 2:
		cnt += randrange(8,10)
	elif len(cv['language']) > 0:
		cnt += 5
		recommendations.append('language')
	else:
		recommendations.append('language')
	if len(cv['position']) >= 5:
		cnt += randrange(8,10)
	elif len(cv['position']) > 0:
		cnt += 5
		recommendations.append('position')
	else:
		recommendations.append('position')
	if len(cv['about']) > 0:
		cnt += 7
	else:
		recommendations.append('about')
	if len(cv['reference']) > 0:
		cnt += 8
	else:
		recommendations.append('reference')    
	cnt += randrange(-1,1)
	if cnt > 100:
		cnt = 100
	if cnt < 0:
		cnt = 0
	return render(request, 'formuploads/rate.html',{"percentage": int(cnt), "reccomendations": recommendations})


def resume(request):
	resume = request.GET.get('resume')

	# resume['firstname'] = 'izat'
	# resume['lastname'] = 'khamiyev'
	# resume['phone'] = '87753809115'
	# resume['email'] = 'izat.khamiyev@nu.edu.kz'
	# resume['address'] = 'Astana, Kabanbay Batyr ave. 53'
	# resume['educations'] = [{'name': 'NU', 'degree': 'Masters', 'start_date': '10.10.2015', 'end_date': '10.10.2017', 'description': 'adsfafd'}, 
	# {'name': 'NU', 'degree': 'Masters', 'start_date': '10.10.2015', 'end_date': '10.10.2017', 'description': 'adsfafd'},
	# {'name': 'NU', 'degree': 'Masters', 'start_date': '10.10.2015', 'end_date': '10.10.2017', 'description': 'adsfafd'}]
	# resume['experiences'] = [{'company_name': 'NU', 'designation': 'Masters', 'start_date': '10.10.2015', 'end_date': '10.10.2017', 'description': 'adsfafd'}]
	# resume['positions'] = ['marketing', 'programming', 'management']
	# resume['skills'] = ['c++','django', 'python']
	# resume['languages'] = [{'name': 'Русский', 'level': 'Изи'}, {'name': 'Казахский', 'level': 'Тяжко'}]
	# resume['about'] = 'asdfoiajdskfalkdsjfakldfmakd'
	print(resume)
	return render(request, 'formuploads/resume.html',{'resume': resume})

