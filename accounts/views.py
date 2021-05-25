from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.models import UserInformation, CollegeName
from django.views.generic.base import TemplateView, RedirectView

def register(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name  = request.POST['last_name']
    username   = request.POST['username']
    email      = request.POST['email']
    password1  = request.POST['password1']
    password2  = request.POST['password2']
    
    if password1 == password2:
      if User.objects.filter(username=username).exists():
          messages.info(request,'Username Already Taken')
          print("---Username Taken---")
          return redirect('register')
      elif User.objects.filter(email=email).exists():
          messages.info(request,'Email Already Taken')
          return redirect('register')
      else:
          user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
          user.save()
          messages.info(request,'User Created')
          print("---User Created---")
          return redirect('login')
    else:
      messages.info(request,'Password Not Matching')
      print("---Password Not Matching---")
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Invalid Credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')


def logout(request):
  auth.logout(request)
  return redirect('/')


def profile(request):
  if request.method == "GET":
    object1 = CollegeName.objects.all()
    context = {'CollegeName': object1}
    return render(request, 'accounts/profile.html', context)
  else:
    Name           = request.POST['name']
    College        = request.POST['college_name']
    CollegeAddress = request.POST['college_address']
    AcademicYear   = request.POST['year']
    Department     = request.POST['department']
    Division       = int(request.POST['division'])
    RollNo         = int(request.POST['roll_no'])
    LinkedIn       = request.POST['linkedIn_url']
    GithubUrl      = request.POST['github_url']
    InstagramUrl   = request.POST['instagram_url']
    Skills         = request.POST['skills']
    Description    = request.POST['description']
    Image          = request.FILES['image']
    userInformation = UserInformation(Name=Name, College=College, CollegeAddress=CollegeAddress, AcademicYear=AcademicYear,
                                      Department=Department, Division=Division, RollNo=RollNo, LinkedIn=LinkedIn,
                                      GithubUrl=GithubUrl, InstagramUrl=InstagramUrl, Skills=Skills, Description=Description, Image=Image)
    userInformation.save()

    messages.info(request,"Success : Profile Saved.")
    print("---Success : Profile Saved---")
    return redirect('profile')
