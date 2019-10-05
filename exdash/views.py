
from django.views.generic import ListView
from django.db.models import Sum

from dailyexpense.models import Expense
class exview(ListView,Expense):
    template_name = "exdash.html"
    model = Expense




