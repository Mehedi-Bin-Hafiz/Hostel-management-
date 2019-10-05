from django.db import models
from django.db.models import Sum

class Expense(models.Model):
    exdate=models.DateField(null=True)
    cost=models.IntegerField(null=True)

    def totalcost(self):
        self.omar=0
        self.total = Expense.objects.aggregate(Sum('cost'))
        for self.j in self.total.values():
            self.omar=self.j
        return self.omar

    def __str__(self):
        return str(self.exdate)