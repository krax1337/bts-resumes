from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "formuploads"
urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name="upload"),
    
    path('search/', views.search_v, name="search"),
    path('generate_pdf/', views.generate_pdf, name="generate_pdf"),
    path('generate_pdf/resume_create/', views.resume_create, name="resume_create"),
    path('upload/show_json/', views.show_json, name="show_json"),
    path('upload/show_xml/', views.show_xml, name="show_xml"),
    path('upload/rate/', views.rate, name = 'rate'),
    path('upload/rate/test', views.test, name="test"),
    path('generate_pdf/resume_create/resume/', views.resume, name="resume"),
    path('generate_pdf/resume_create/extract_pdf/', views.extract_pdf, name="extract_pdf"),
    
]
