from operator import mod
from django import forms
from . import models
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class ProfileForm(forms.MOdelForm):
    class Meta:
        model = models.Profile
        fields = ['image','address']