from django.shortcuts import render
from .models import Project

def home(request):
    # Fetch all projects from the database
    projects = Project.objects.all()
    # Pass the projects into the HTML template via a dictionary context
    return render(request, 'portfolio/home.html', {'projects': projects})