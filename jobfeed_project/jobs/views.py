from django.http import HttpResponse
from .models import Job
from django.template.loader import render_to_string
from django.utils import timezone
from django.shortcuts import render

def job_feed(request):
    jobs = Job.objects.all()
    xml = render_to_string('jobs/job_feed.xml', {'jobs': jobs})
    return HttpResponse(xml, content_type='application/xml')

def home(request):
    return HttpResponse("Welcome to the Job Feed Application! Visit /jobs/feed/ to view the XML job feed.")

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})
