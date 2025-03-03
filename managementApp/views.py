import datetime
import os
# Calling inbuilt django models
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from managementApp.EmailBackEnd import EmailBackEnd
from UniversityManagementSystem import settings

from managementApp.forms import RegisterUserForm
from managementApp.models import RegisterUser
# To Demo Page
def showDemoPage(req):
    return render(req,"demo.html")

# To Render Login Page
def ShowLoginPage(req):
    return render(req,"login_page.html")

# To Auth the User via email and password
import logging

logger = logging.getLogger(__name__)

import logging

logger = logging.getLogger(__name__)

def doLogin(req):
    if req.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        email = req.POST.get("email")
        password = req.POST.get("password")
        email = req.POST.get("email")
        password = req.POST.get("password")
        user = authenticate(req, username=email, password=password)
        if user!=None:
            login(req,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            logger.warning(f"Invalid login attempt for email: {email}")
            logger.warning(f"Invalid login attempt for email: {email}")
            messages.error(req, "Invalid Login Details")
            return HttpResponseRedirect("/")

# For Demo Usage
def GetUserDetails(req):
    if req.user!=None:
        return HttpResponse("User : "+req.user.email+" usertype : "+str(req.user.user_type))
    else:
        return HttpResponse("Please Login First")

# To Logout User
def logout_user(req):
    logout(req)
    return HttpResponseRedirect("/")

def registerPage(req):
    if req.method!='POST':
        form=RegisterUserForm()
        return render(req,'registration/register_page.html',{'form':form})
    else:
        # import pdb; pdb.set_trace()
        form=RegisterUserForm(req.POST)
        if form.is_valid():
            # Takeing data from the form
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            email=form.cleaned_data["email"]
            password=make_password(form.cleaned_data["password"])
            address=form.cleaned_data["address"]
            user_type=form.cleaned_data["user_type"]
            try:
                rguser=RegisterUser.objects.create(password=password,email=email,last_name=last_name,first_name=first_name,user_type=user_type,address=address)
                rguser.save()
                messages.success(req,"Successfully! wait for admin response")
                return HttpResponseRedirect('/')
            except:
                messages.error(req,"Failed! Username or Email is already present")
                return HttpResponseRedirect('/')
