from django.views.generic import ListView
from django.contrib.auth.models import User

class userproview(ListView):
    template_name = "userpro.html"
    model =  User
