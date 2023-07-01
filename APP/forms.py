from django.forms import ModelForm
from APP.models import *
from django.contrib.auth.models import User

# First of all create MODELFORM for 'user' object at first, to put details on the form page
class Userform(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

# Creating a MODELFORM for 'person' model --
# which means a form will automatically be created based on the model attributes

class Personform(ModelForm): 
    class Meta:
        model = Person   
        fields = '__all__'  # All attributes of 'Person' model and thus 'user' model are necessary to fill
        