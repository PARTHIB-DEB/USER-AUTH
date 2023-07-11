from django.urls import path
from APP import views

urlpatterns = [
    path("",views.root,name="root"), # RootPage Url
    path("sin/",views.register,name="sin"), # Register account Url
    path("sout/",views.signOut,name="sout"), # Destroy account Url
    path("lin/",views.logIn,name="lin"), # Activate account Url
    path("lout/",views.logOut,name="lout"), # Deactivate account Url
]