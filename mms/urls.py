"""mms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mealinput.views
import dailyexpense.views
import mealdashboard.views
import exdash.views
import index.views
import signup.views
import login.views
import manager.views
import userpro.views
import deposit.views
import depodash.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index.views.indexview,name="index"),
    path('mealinput/', mealinput.views.mealinputformview, name="mealinput"),
    path('expense/', dailyexpense.views.expenseformview, name="dailyexpense"),
    path('deposit/', deposit.views.depositview, name="deposit"),
    path('ddash/', depodash.views.depoview.as_view(), name="depodash"),
    path('dashboard/', mealdashboard.views.mealview.as_view(), name="mealdashboard"),
    path('edash/', exdash.views.exview.as_view(), name="exdash"),
    path('signup/',signup.views.signupview,name="signup"),
    path('login/',login.views.loginview,name="login"),
    path('manager/',manager.views.managerview.as_view(),name='manager'),
    path('userpro/',userpro.views.userproview.as_view(),name='userpro'),
    path('logout/', index.views.logout, name="logout"),

]
