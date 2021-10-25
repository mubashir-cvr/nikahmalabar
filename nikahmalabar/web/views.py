from django.http.response import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from user.models import Image, UserEducationLocationContact,UserProperties,User
from user.forms import UserPropertiesForm
from web.models import Profile


def index(request):
    context = {
        "is_index" : True
    }
    return render(request, 'web/index.html',context) 


def login(request): 
    context = {
        "is_login" : True
    }
    return render(request, 'web/login.html',context) 


def signup(request): 
    context = {
        "is_signup" : True 
    }
    return render(request, 'web/signup.html',context) 


def profiler(request): 
    form = UserPropertiesForm(request.POST or None)
    context = {
        "is_profiler" : True,
        "form":form
    }
    return render(request, 'web/profiler.html',context) 

def profilerB(request): 
    
    context = {
        "is_profilerB" : True 
    }
    return render(request, 'web/profilerB.html',context) 


def imageupload(request): 

    if request.method == 'POST':


        image = request.FILES.get('image')
        email = request.POST.get('email1')
        user =   User.objects.filter(email=email).first()
        education= UserEducationLocationContact.objects.filter(user=user).first()
        profile= UserProperties.objects.filter(user=user).first()
        print(user)
        data = Image()
            
        data.image = image
        data.user = user
        data.education=education
        data.profile=profile
        data.save()

        return redirect ('web:home')
    return render(request, 'web/imageupload.html',) 



def home(request):
    profileimage = Image.objects.all()
    userproperties = UserProperties.objects.all()
    profile = Profile.objects.all()
    context = {
        "is_home" : True,
        "profileimage":profileimage,
        "userproperties":userproperties,
        "profile":profile
    }
    print(profileimage)
    return render(request, 'web/home.html',context) 
