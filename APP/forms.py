from django.forms import ModelForm
from APP.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Creating MODELFORM for 'user' object at first, to put details on the form page
class Signform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']  

# Have to create another version of UserCreationForm for Login
# fields = ['username','password']


# Creating a MODELFORM for 'person' model --
class Dobform(ModelForm): 
    class Meta:
        model = Person   
        fields = '__all__' 
        