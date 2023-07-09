from django.urls import path
from APP.views import *

urlpatterns = [
    path("",root,name="root"),
    path("sin/<str:pk>/",register,name="sin"),
    path("sout/<str:pk>/",signOut,name="sout"),
    path("lin/<str:pk>/",logIn,name="lin"),
    path("lout/<str:pk>/",logOut,name="lout"),
]