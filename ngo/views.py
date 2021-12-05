from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from .models import *

# Create your views here.
@csrf_exempt
def index(request):
    #ngos=NGO.objects.all()
    ngos = Organization.objects.raw('select * from ngo_organization')
    data={'ngos':ngos}
    return render(request, 'index.html',data)

@csrf_exempt
def register_ngo(request):
    if request.method == "POST":
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        location=request.POST['location']
        phone=request.POST['phone']
        description=request.POST['description']
        links=request.POST['links']
        logo=request.FILES['logo']
        if password==confirm_password:
            #if Organization.objects.raw('select * from ngo_organization where username={};'.format(username)):
            if Organization.objects.filter(username=username).exists():
                #return JsonResponse({'Login':'Username taken'})
                messages.info(request,'Username Taken')
                return redirect('/register-ngo/')
            #elif Organization.objects.raw('select * from ngo_organization where email={};'.format(email)):
            elif Organization.objects.filter(email=email).exists():
                #return JsonResponse({'Login':'Email taken'})
                messages.info(request,'Email Taken')
                return redirect('/register-ngo/')
            else:
                #user=Organization.objects.raw('insert into ngo_organization (username,password,email,name,location,phone,description,links,logo) values ({},{},{},{},{},{},{},{},{})'.format(username,password,email,name,location,phone,description,links,logo))
                user=Organization.objects.create_user(username=username,password=password,email=email,name=name,location=location,phone=phone,description=description,links=links,logo=logo)
                user.save()
                messages.info(request,'Success')
                return redirect('/login-ngo/')
        else:
            messages.info(request,'Password does not match')
            print("Password no")
            return redirect('/register-ngo/')
    return render(request,'register_ngo.html')

def login_ngo(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        #user=Organization.objects.raw("SELECT * FROM ngo_organization WHERE username={}".format(username))
        user=Organization.objects.get(username=username)
        if(user.check_password(password)):
            auth.login(request,user)
            print(user.is_authenticated)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            print("Wrong",username,password,user)
            return redirect('/login-ngo/')
    else:
        return render(request,"login_ngo.html")

def logout_ngo(request):
    print(request.user.is_authenticated)
    auth.logout(request)
    print(request.user.is_authenticated)
    return redirect('/')