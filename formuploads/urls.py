from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "formuploads"
urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name="upload"),
    path('upload/show_json/', views.show_json, name="show_json"),
    path('upload/show_xml/', views.show_xml, name="show_xml"),
]
