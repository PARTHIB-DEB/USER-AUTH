from django.shortcuts import render
from APP.forms import *
from django.contrib.auth.models import User
# Create your views here.
def signin(request):  # Function for Signing NEW USER
    # Individual logic for --
    # 1) 'User' object (username, firstname,lastname,password,email) MAYBE A DIFFERENT PAGE NEEDED!!
    # 2) 'Person' object (Date of birth)
    return render(request,"signin.html")
        


def signout(request):  # Function for deleting account / signing out a USER
    return render(request,"signout.html")


def login(request):   # Function to give entry permission to AUTHENTICATED USER
    return render(request,"login.html")


def logout(request):  # Function for temporarily disabling one AUTHENTICATED USER's account
    return render(request,"logout.html")


