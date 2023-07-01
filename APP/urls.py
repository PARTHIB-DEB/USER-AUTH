from django.urls import path
from APP.views import *

urlpatterns = [
    path("",signin,name="SIGNIN"),
    path("s-out",signout,name="SIGNIN"),
    path("l-in",login,name="SIGNIN"),
    path("l-out",logout,name="SIGNIN"),
]