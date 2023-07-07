from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    Personal_details=models.OneToOneField(User,on_delete=models.CASCADE)
    Date_of_Birth=models.DateField()