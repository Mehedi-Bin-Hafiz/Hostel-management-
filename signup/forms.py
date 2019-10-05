from django.contrib.auth.models import User
from django import forms

class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']