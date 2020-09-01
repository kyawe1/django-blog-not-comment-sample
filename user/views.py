from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout as django_logout,login as django_login
from django.http import HttpRequest,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
# Create your views here.

@csrf_protect
def login(request:HttpRequest):
    if (request.method=='POST'):
        user=authenticate(request,username=request.POST['name'],password=request.POST['password'])
        
        if user is not None:
            django_login(request,user)
            return redirect('normal:home')
    return render(request,'user/login.html')
@login_required
def logout(request:HttpRequest):
    django_logout(request)
    return redirect('normal:home')
@csrf_protect
def register(request:HttpRequest):
    if (request.method=='POST'):
        print(request.POST)
    return render(request,'user/register.html')


