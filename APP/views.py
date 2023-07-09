from django.contrib import messages
from django.shortcuts import render, HttpResponse
from APP.forms import *

# Create your views here.
def root(request):
    return render(request,"rootPage.html")


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password=request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user=User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        return render(request,'rootPage.html')
    else:
        return render(request, 'signIn.html')


def signOut(request):
    return HttpResponse("<h1>DELETE ACCOUNT</h1>")


def logIn(request, pk):
    return HttpResponse("<h1>REACTIVATE</h1>" + str(pk))


def logOut(request, pk):
    return HttpResponse("<h1>DEACTIVATE</h1>" + str(pk))
