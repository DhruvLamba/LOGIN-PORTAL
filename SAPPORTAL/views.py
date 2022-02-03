from cgitb import html
from html.entities import html5
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Create your views here.
def indexUser (request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
           login(request,user)
           return redirect("/main")
        # A backend authenticated the credentials
        else:
           return render(request,'index.html')

           
        
       # No backend authenticated the credentials
      
    
    return render(request,'index.html')

def about(request):
    if request.user.is_anonymous:
      return redirect("/")


    return render(request,'main.html')

def logoutuser(request):
    logout(request)
    return redirect("/")