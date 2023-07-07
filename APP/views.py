from django.shortcuts import render
from APP.forms import *
from django.contrib.auth.models import User
from APP.models import *

# Create your views here.


def rootPage(request):
    return render(request, "rootPage.html")


def signIn(request):  # Function for Signing NEW USER
    form = Signform()  # Creating an empty form (for requests apart from POST)
    Dob_details = Dobform() # Creating an empty form (for requests apart from POST)
    if request.method == "POST":
        form = Signform(request.POST)
        Dob_details = Dobform(request.POST)
        # username = request.POST["username"]
        # first_name = request.POST["first_name"]
        # last_name = request.POST["last_name"]
        # email = request.POST["email"]
        # password = request.POST["password"]
        # Date_of_Birth = request.POST["Date_of_Birth"]
        if form.is_valid() and Dob_details.is_valid():
            Personals = form.save()
            DateOfBirth = Dob_details.save()
            DateOfBirth.Personal_details = Personals
            form.cleaned_data["username"]
            form.cleaned_data["first_name"]
            form.cleaned_data["last_name"]
            form.cleaned_data["email"]
            form.cleaned_data["password"]
            Dob_details.cleaned_data["Date_of_Birth"]
        # obj = User.objects.create(
        #     username=username,
        #     first_name=first_name,
        #     last_name=last_name,
        #     email=email,
        #     password=password,
        # )
        # Person.objects.create(Personal_details=obj, Date_of_Birth=Date_of_Birth)
    context = {"form": form, "Dob": Dob_details}
    return render(request, "signIn.html", context)


def sinRes(
    request,
):  # Throwing a response page that new account has been created successfully!!
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
