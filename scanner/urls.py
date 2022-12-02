from django.conf.urls import include
from django.urls import path, re_path
from . import views

app_name = 'scanner'

urlpatterns = [
    path('', views.create, name='create'),
]