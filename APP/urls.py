from django.urls import path
from APP.views import *

urlpatterns = [
    
    # Maybe one more HTML PAGE for seperately filling USER DETAILS --> Convert it into ROOT PATH
    
    path("",rootPage,name="root"),
    path("sin/",signIn,name="sin"),
    path("sinr/",sinRes,name="sinr"),
    path("sout/",signOut,name="sout"),
    path("soutr/",soutRes,name="soutr"),
    path("lin/",logIn,name="lin"),
    path("linr/",linRes,name="linr"),
    path("lout/",logOut,name="lout"),
    path("loutr/",loutRes,name="loutr"),
]