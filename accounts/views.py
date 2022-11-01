from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.postgres import *
from .models import *
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"this username is already taken,try another one")
                return redirect('reg/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"this email is already taken,try another one")
                return redirect('reg/')
            else:
               user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
               user.save()
               print("user created")
               return redirect('reg')
        else:
            messages.info(request,"password is not matching,try again")
            return redirect('reg')
    else:
        return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid details')
            return redirect('login')
    else:
        return render(request,"login.html")