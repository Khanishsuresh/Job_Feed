# jobs/urls.py
from django.urls import path
from .views import job_feed, job_list

urlpatterns = [
    path('feed/', job_feed, name='job_feed'),
    path('list/', job_list, name='job_list'),
]
