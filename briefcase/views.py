from django.shortcuts import render
from django.http import HttpResponse
from briefcase.models import Bio, Skill, Project


def employeeinfo(request):
    emp = Bio.objects.all()
    return render(request, 'index.html', {'em': emp[1]})


def about(request):
    emp1 = Bio.objects.all()
    queryset = Skill.objects.filter().values()
    # projects = Project.objects.filter().values()
    # print(projects)
    return render(request, 'about.html', {'em1': emp1[1], 'skills': queryset})


def about1(request):
    projects = Project.objects.filter().values()
    print(projects)
    return render(request, 'about1.html', {'project': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def resume(request):
    return render(request, 'resume.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')

# Create your views here.
