
from django.views.generic import ListView
from django.db.models import Sum

from deposit.models import Deposit
class depoview(ListView,Deposit):
    template_name = "ddash.html"
    model = Deposit




