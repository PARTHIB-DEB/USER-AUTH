from django.shortcuts import render, HttpResponse


# Create your views here.
def root(request):
    return HttpResponse("<h1>ROOT PAGE</h1>")


def register(request, pk):
    return HttpResponse("<h1>REGISTER PAGE</h1>" + str(pk))


def signOut(request, pk):
    return HttpResponse("<h1>DELETE ACCOUNT</h1>" + str(pk))


def logIn(request, pk):
    return HttpResponse("<h1>REACTIVATE</h1>" + str(pk))


def logOut(request, pk):
    return HttpResponse("<h1>DEACTIVATE</h1>" + str(pk))
