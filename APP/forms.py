from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Creating MODELFORM for 'user' object at first, to put details on the form page
class Signform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        

# Have to create another version of UserCreationForm for Login
# fields = ['username','password']
        
        
        