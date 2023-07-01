from django.shortcuts import render,HttpResponse

# Create your views here.
def signin(request):  # Function for Signing NEW USER
    return HttpResponse("<h1>SIGN-IN PAGE</h1>")


def signout(request):  # Function for deleting account / signing out a USER
    return HttpResponse("<h1>SIGN-OUT PAGE</h1>")


def login(request):   # Function to give entry permission to AUTHENTICATED USER
    return HttpResponse("<h1>LOG-IN PAGE</h1>")


def logout(request):  # Function for temporarily disabling one AUTHENTICATED USER's account
    return HttpResponse("<h1>LOG-OUT PAGE</h1>")


