from .models import myusers
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class NewUserForm(forms.ModelForm):
    stock = forms.CharField(label='stock', max_length=100)
    class Meta:
        model = myusers
        fields = ["stock"]

