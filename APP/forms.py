from django.forms import ModelForm
from APP.models import *

# Creating a MODELFORM for 'person' model --
# which means a form will automatically be created based on the model attributes

class Personform(ModelForm):
    class Meta:
        model = Person   
        fields = '__all__'  # All attributes of 'Person' model and thus 'user' model are necessary to fill
        