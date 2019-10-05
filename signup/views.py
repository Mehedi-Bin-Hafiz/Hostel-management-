from django.shortcuts import render,redirect,HttpResponse,reverse,HttpResponsePermanentRedirect
from .forms import signupform    # signupform is a class of forms.py
from django.views.generic import View
from django.contrib.auth import authenticate,login

from django.contrib.auth.models import User

def signupview(request):
    form=signupform(request.POST or None)  #we import class signupform and create form as an object
    if request.method=='GET':
        return render(request, 'signup.html', {'form': form})
    elif request.method=='POST':
        form = signupform(request.POST or None)
        if form.is_valid():  # is_valid used for fill all the field
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, email=email, password=password)
            user.set_password(password)
            user.is_active = True
            user.save()
            user = authenticate(username=username, password=password, email=email)
            if user is not None:
             if user.is_active:
                login(request, user)
                return HttpResponsePermanentRedirect(reverse('userpro'))  # here userpro is an app name
                # It is the power of name and namespase
        else:
            print(form.errors)
            return render(request, 'signup.html', {'form': form})

    else:return render(request, 'signup.html', {'form': form})

          # user authentication



