from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,JsonResponse
import random
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as LOGIN ,logout as LOGOUT,authenticate
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,"index.html")
def create_manager(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        company_name = request.POST['company_name']
        company_website = request.POST['company_website']
        company_id = Manager.objects.all().count() + 1 #for make every compnay uniq in this system
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # hasing password
        password = make_password(request.POST['password'])
        email = request.POST['email']
        username = request.POST['email'] #set username fields as email we will use django defult django authentication
        
        try:
            manager = Manager.objects.create(company_name=company_name,
                    company_website=company_website,company_id=company_id,
                    first_name=first_name,last_name=last_name,password=password,email=email,username=username)

            manager.save()
            return redirect('login')
            
        except:
            return render(request,"index.html",{"msg":"input are not valid"})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        return render(request,"login.html",{"msg":"input are not valid"})
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        res = authenticate(username=username,password=password)
        if(res is None):
            return HttpResponse("<h1>Acuthentication error!!!<h1>")
        else:
            LOGIN(request,res) 
            return redirect("home")

def logout(request):
    LOGOUT(request)
    return render(request,"index.html")

@login_required
def home(request):
    return render(request,"home.html")