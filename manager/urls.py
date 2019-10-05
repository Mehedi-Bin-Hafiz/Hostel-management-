from django.urls import path
from .import views
import signup.views
import login.views
import deposit.views
import depodash.views

urlpatterns = [
    path('',views.indexview,name="index"),
    # path('about/',about.views.aboutview.as_view(),name="about"),
    path('signup/',signup.views.signupview,name="signup"),
    path('login/',login.views.loginview,name="login"),
    path('manager',views.managerviews.as_view(),name='manager'),
    path('deposit/', deposit.views.depositview, name="deposit"),



]