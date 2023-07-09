from django.urls import path
from APP import views

urlpatterns = [
    path("",views.root,name="root"),
    path("sin/",views.register,name="sin"),
    path("sout/",views.signOut,name="sout"),
    path("lin/<str:pk>/",views.logIn,name="lin"),
    path("lout/<str:pk>/",views.logOut,name="lout"),
]