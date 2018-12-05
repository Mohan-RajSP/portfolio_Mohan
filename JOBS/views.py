from django.shortcuts import render
from .models import Job

def home(request):
    job = Job.objects

    return render(request, 'Jobs/home.html', {'job': job})

# Create your views here.