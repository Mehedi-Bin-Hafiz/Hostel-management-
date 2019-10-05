from django.contrib import admin

# Register your models here.
from .models import Expense
admin.site.register(Expense)

# We need to register our models here when we need to show it on Django admin