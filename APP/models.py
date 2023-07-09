from django.db import models

# Create your models here.

class RegisterModel(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=1000)
    password1=models.CharField(max_length=8)
    password2=models.CharField(max_length=8)
    first_name=models.TextField()
    last_name=models.TextField()
    
    def __str__(self) -> str:
        return self.username
