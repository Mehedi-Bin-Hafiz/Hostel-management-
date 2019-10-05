
from django.views.generic import ListView

from mealinput.models import MealInput
class mealview(ListView):
    template_name = "mealdashboard.html"
    model = MealInput  # we import MealInput model here



    # This note belongs to html file
    # {{'<!--'}} this is used for break the line
    # when we use it, this is print just for one time