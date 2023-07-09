from django import forms
from APP.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.ModelForm):
    # Creating a Form by ModelForm class from Model RegisterModel

    # password1=forms.CharField(widget=forms.PasswordInput)
    # password2=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegisterModel
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

    def passwords_validate(self):  # Validating password attribute
        pass1 = self.cleaned_data["password1"]
        pass2 = self.cleaned_data["password2"]

        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError("Password don't match")
        return pass1

    # Defining the Save method of RegisterUserForm

    def save(self, commit=True):
        user = User.objects.create(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password1"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
        )
        return user
