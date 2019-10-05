from django.shortcuts import render,redirect
from django.contrib import auth

def indexview(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return  redirect('/')
