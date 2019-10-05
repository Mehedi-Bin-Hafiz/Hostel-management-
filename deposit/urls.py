
from django.urls import path

import deposit.views

urlpatterns = [
    path('deposit/', deposit.views.depositview, name="deposit"),

]
