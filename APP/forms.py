from django.forms import ModelForm
from APP.models import *
from django.contrib.auth.models import User

# Creating MODELFORM for 'user' object at first, to put details on the form page
class Userform(ModelForm):
    class Meta:
        model = User
        fields = '__all__'  # All attributes of 'user' model and thus 'user' model are necessary to fill

# Creating a MODELFORM for 'person' model --
class Personform(ModelForm): 
    class Meta:
        model = Person   
        fields = '__all__'  # All attributes of 'Person' model and thus 'user' model are necessary to fill
        