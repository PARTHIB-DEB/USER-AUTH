from django.urls import path
from APP.views import *

urlpatterns = [
    
    # Maybe one more HTML PAGE for seperately filling USER DETAILS --> Convert it into ROOT PATH
    
    path("",signin,name="SIGNIN"),
    path("s-out",signout,name="SIGNIN"),
    path("l-in",login,name="SIGNIN"),
    path("l-out",logout,name="SIGNIN"),
]