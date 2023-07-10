from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User

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
        try:  # Validating Only based on Username!! Need some kore individual Validations for some of the attributes
            user=User.objects.create_user(username,email,password)
            user.first_name=first_name
            user.last_name=last_name
            user.save()
            messages.success(request,f" {username} , Your account has been created!!")
            return redirect("/")
        except Exception:
            messages.warning(request,f"Object of Username {username} Already exists")
            return render(request,"signIn.html")
    else:
        return render(request, 'signIn.html')


def signOut(request):
    if request.method == "POST":
        uname=request.POST['username']
        try:
            User.objects.get(username=uname).delete()
            messages.success(request,f"Object of username :{uname} is deleted!!")
            return render(request,"rootPage.html")
        except Exception:
            messages.success(request,f"Object of Username {uname} Doesnot exists")
            return render(request,"rootPage.html")
    return render(request,"signOut.html")


def logIn(request, pk):
    return HttpResponse("<h1>REACTIVATE</h1>" + str(pk))


def logOut(request, pk):
    return HttpResponse("<h1>DEACTIVATE</h1>" + str(pk))
