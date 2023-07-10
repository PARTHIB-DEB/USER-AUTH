from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.ModelForm):
    # Creating a Form by ModelForm class from Model RegisterModel

    # password1=forms.CharField(widget=forms.PasswordInput)
    # password2=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = "__all__"

    # Methods of Validating different attributes of RegisterModel/RegisterUserForm
    # We will get each result in views by calling them

    def username_validate(self):  # Validating username attribute
        uname = self.cleaned_data["username"]
        queryset = User.objects.filter(username=uname)
        if queryset.count():
            raise ValidationError("User already Exists")
        return uname

    def email_validate(self):  # Validating email attribute
        email = self.cleaned_data["email"]
        queryset = User.objects.filter(email=email)
        if queryset.count():
            raise ValidationError(" Email Already Exist")
        return email

    # Defining the Save method of RegisterUserForm

