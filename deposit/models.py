from django.db import models
from django.db.models import Sum
from mealinput.models import MealInput
from dailyexpense.models import Expense

class Deposit(models.Model):
    mehedidepo = models.FloatField(null=True)
    omardepo = models.FloatField(null=True)
    shafindepo = models.FloatField(null=True)
    bikidepo = models.FloatField(null=True)
    nurudepo = models.FloatField(null=True)
    abirdepo = models.FloatField(null=True)

    def mtotalcost(self):  # mtotalcost means mehedi's deposited money
        self.total = Deposit.objects.aggregate(Sum('mehedidepo'))
        for self.j in self.total.values():
           return self.j

    def ototalcost(self):   # ototalcost means omar's deposited money
        self.total = Deposit.objects.aggregate(Sum('omardepo'))
        for self.j in self.total.values():
           return self.j

    def stotalcost(self):
        self.total = Deposit.objects.aggregate(Sum('shafindepo'))
        for self.j in self.total.values():
           return self.j

    def btotalcost(self):
        self.total = Deposit.objects.aggregate(Sum('bikidepo'))
        for self.j in self.total.values():
           return self.j

    def ntotalcost(self):
        self.total = Deposit.objects.aggregate(Sum('nurudepo'))
        for self.j in self.total.values():
           return self.j

    def atotalcost(self):
        self.total = Deposit.objects.aggregate(Sum('abirdepo'))
        for self.j in self.total.values():
           return self.j


    def depomealrate(self):
        self.mrate = MealInput
        self.rate=self.mrate.mealrate(self)
        return self.rate

    # mmc = mehedi meal cost
    def mmc(self):
        self.monthlycost = MealInput.mehedimeal(self) * self.depomealrate()
        return round(float(self.monthlycost), 3)

    def omc(self):
        self.monthlycost = MealInput.omarmeal(self) * self.depomealrate()
        return round(float(self.monthlycost), 3)

    def smc(self):
        self.monthlycost = MealInput.shafinmeal(self) * self.depomealrate()
        return round(float(self.monthlycost), 3)

    def bmc(self):
        self.monthlycost = MealInput.bikimeal(self) * self.depomealrate()
        return round(float(self.monthlycost), 3)

    def nmc(self):
       self.monthlycost = MealInput.nurumeal(self) * self.depomealrate()
       return round(float(self.monthlycost), 3)

    def amc(self):
       self.monthlycost = MealInput.abirmeal(self) * self.depomealrate()
       return round(float(self.monthlycost), 3)

    # mgp = mehedi get or pay

    def mgp(self):
        self.mehedigp = Deposit.mtotalcost(self) - Deposit.mmc(self)
        return round(float(self.mehedigp), 3)

    def ogp(self):
        self.omargp = Deposit.ototalcost(self) - Deposit.omc(self)
        return round(float(self.omargp), 3)

    def sgp(self):
        self.shafingp = Deposit.stotalcost(self) - Deposit.smc(self)
        return round(float(self.shafingp), 3)

    def bgp(self):
        self.bikigp = Deposit.btotalcost(self) - Deposit.bmc(self)
        return round(float(self.bikigp), 3)

    def ngp(self):
        self.nurugp = Deposit.ntotalcost(self) - Deposit.nmc(self)
        return round(float(self.nurugp), 3)

    def agp(self):
        self.abirgp = Deposit.atotalcost(self) - Deposit.amc(self)
        return round(float(self.abirgp), 3)

