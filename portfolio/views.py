from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/home.html', {
        'name': 'Pala Peshmarga',
        'projects': projects
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})