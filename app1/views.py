from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.models import UserInformation

def home(request):
  object1 = UserInformation.objects.all()
  context = {'user_info': object1}
  return render(request, 'app1/home.html', context)


def header(request):
  return render(request, 'header.html')


def search(request):
  if request.method == 'POST':
    result = None
    search = request.POST['search']
    search_filter = request.POST['search_filter']
    if search_filter=='Name' and UserInformation.objects.filter(Name__icontains=search):
      result = UserInformation.objects.filter(Name__icontains=search)
    elif search_filter=='College' and UserInformation.objects.filter(College__icontains=search):
      result = UserInformation.objects.filter(College__icontains=search)
    elif search_filter=='CollegeAddress' and UserInformation.objects.filter(CollegeAddress__icontains=search):
      result = UserInformation.objects.filter(CollegeAddress__icontains=search)
    elif search_filter=='AcademicYear' and UserInformation.objects.filter(AcademicYear__icontains=search):
      result = UserInformation.objects.filter(AcademicYear__icontains=search)
    elif search_filter=='Department' and UserInformation.objects.filter(Department__icontains=search):
      result = UserInformation.objects.filter(Department__icontains=search)
    elif search_filter=='Division' and UserInformation.objects.filter(Division__icontains=search):
      result = UserInformation.objects.filter(Division__icontains=search)
    elif search_filter=='RollNo' and UserInformation.objects.filter(RollNo__icontains=search):
      result = UserInformation.objects.filter(RollNo__icontains=search)
    elif search_filter=='LinkedIn' and UserInformation.objects.filter(LinkedIn__icontains=search):
      result = UserInformation.objects.filter(LinkedIn__icontains=search)
    elif search_filter=='GithubUrl' and UserInformation.objects.filter(GithubUrl__icontains=search):
      result = UserInformation.objects.filter(GithubUrl__icontains=search)
    elif search_filter=='InstagramUrl' and UserInformation.objects.filter(InstagramUrl__icontains=search):
      result = UserInformation.objects.filter(InstagramUrl__icontains=search)
    elif search_filter=='Skills' and UserInformation.objects.filter(Skills__icontains=search):
      result = UserInformation.objects.filter(Skills__icontains=search)
    else:
      return render(request, 'search.html', {'search_filter': search_filter, 'search': search, 'result': result})
    return render(request, 'search.html', {'search_filter': search_filter, 'search': search, 'result': result})
  else:
    return render(request, 'search.html')
