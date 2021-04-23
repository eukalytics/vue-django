from django.shortcuts import render
from django.http import HttpResponse

from .models import Course

# Create your views here.

def courses(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'courses/courses.html', context)