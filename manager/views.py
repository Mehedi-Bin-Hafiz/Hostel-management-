from django.views.generic import ListView
from django.contrib.auth.models import User

class managerview(ListView):
    template_name = "manager.html"
    model =  User
