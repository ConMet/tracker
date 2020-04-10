from django.shortcuts import render
from projects.models import Project


def homepage(request):
    return render(request, 'homepage.html', {})
