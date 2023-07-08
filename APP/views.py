from django.shortcuts import render, redirect
from APP.forms import *
from django.contrib.auth.models import User
from APP.models import *

# Create your views here.


def rootPage(request):
    return render(request, "rootPage.html")


def signIn(request):  # Function for Signing NEW USER
    pass

def sinRes(request):
    return render(request, "sinRes.html")


def signOut(request):  # Function for deleting account / signing out a USER
    return render(request, "signOut.html")


def soutRes(
    request,
):  # Throwing a response page that the specified account has been deleted successfully!!
    return render(request, "soutRes.html")


def logIn(request):  # Function to give entry permission to AUTHENTICATED USER
    return render(request, "logIn.html")


def linRes(
    request,
):  # Throwing a response page that an AUTHENTICATED person has re-entered successfully!!
    return render(request, "linRes.html")


def logOut(
    request,
):  # Function for temporarily disabling one AUTHENTICATED USER's account
    return render(request, "logOut.html")


def loutRes(
    request,
):  # Throwing a response page that an AUTHENTICATED person is temporarily out successfully!!
    return render(request, "loutRes.html")
