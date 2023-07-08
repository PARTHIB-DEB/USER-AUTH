from django.forms import ValidationError
from django.shortcuts import render, redirect
from APP.forms import *
from django.contrib.auth.models import User

# Create your views here.


def rootPage(request):
    return render(request, "rootPage.html")


def signIn(request):  # Function for Signing NEW USER
    if request.method == "POST":
        form = Signform(request.POST)
        if form.is_valid():
            form.save()
            pass1 = form.cleaned_data["password1"]
            pass2 = form.cleaned_data["password2"]
            if pass1 ==  pass2:
                User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=pass1,
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            else:
                raise ValidationError("Password Don't Match!!")
    else:
        form = Signform()
    
    return render(request, "signIn.html", {"form": form})


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
