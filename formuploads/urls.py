from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "formuploads"
urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name="upload"),
    path('upload/test/', views.show_json, name="test"),
    path('upload/show_json/', views.test, name="show_json"),
    path('upload/show_xml/', views.show_xml, name="show_xml"),
]
