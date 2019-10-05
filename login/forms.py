from django import forms
from django.shortcuts import render
from django.core.exceptions import ValidationError
class Loginuser(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)