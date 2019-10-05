from django.db import models
from dailyexpense.models import Expense
from django.db.models import Sum

class MealInput(models.Model):    # we created here a database table for mealinput
    date=models.DateField(null=True)
    mehedil=models.IntegerField(null=True)
    mehedid=models.IntegerField(null=True)
    omarl=models.IntegerField(null=True)
    omard=models.IntegerField(null=True)
    shafinl=models.IntegerField(null=True)
    shafind=models.IntegerField(null=True)
    bikil=models.IntegerField(null=True)
    bikid=models.IntegerField(null=True)
    nurul=models.IntegerField(null=True)
    nurud=models.IntegerField(null=True)
    abirl=models.IntegerField(null=True)
    abird=models.IntegerField(null=True)


    def mehedimeal(self):   # this function is used for calculate the total meal of each person
        self.totald=0
        self.totall=0
        self.sumtotald=0
        self.sumtotall=0
        self.totall = MealInput.objects.aggregate(Sum('mehedil'))  # we used sql sum by importing from django.db.models import Sum
        self.totald= MealInput.objects.aggregate(Sum('mehedid'))   # here aggregate function made the sum as dictionary
        for self.j in self.totall.values():           # here self.totall is dictionary, by using for loop we get single value
           self.sumtotall= self.j  # here self.sumtotall stored the single column's total(summation) values
        for self.q in self.totald.values():
           self.sumtotald= self.q
        return self.sumtotald+self.sumtotall

    def omarmeal(self):  # this function is used for calculate the total meal of each person
        self.totald=0
        self.totall=0
        self.sumtotald=0
        self.sumtotall=0
        self.totall = MealInput.objects.aggregate(Sum('omarl'))
        self.totald= MealInput.objects.aggregate(Sum('omard'))
        for self.j in self.totall.values():
           self.sumtotall= self.j
        for self.q in self.totald.values():
           self.sumtotald= self.q
        return self.sumtotald+self.sumtotall

    def shafinmeal(self):  # this function is used for calculate the total meal of each person
        self.totald=0
        self.totall=0
        self.sumtotald=0
        self.sumtotall=0
        self.totall = MealInput.objects.aggregate(Sum('shafinl'))
        self.totald= MealInput.objects.aggregate(Sum('shafind'))
        for self.j in self.totall.values():
           self.sumtotall= self.j
        for self.q in self.totald.values():
           self.sumtotald= self.q
        return self.sumtotald+self.sumtotall

    def bikimeal(self):  # this function is used for calculate the total meal of each person
        self.totald=0
        self.totall=0
        self.sumtotald=0
        self.sumtotall=0
        self.totall = MealInput.objects.aggregate(Sum('bikil'))
        self.totald= MealInput.objects.aggregate(Sum('bikid'))
        for self.j in self.totall.values():
           self.sumtotall= self.j
        for self.q in self.totald.values():
           self.sumtotald= self.q
        return self.sumtotald+self.sumtotall

    def nurumeal(self):  # this function is used for calculate the total meal of each person
        self.totald=0
        self.totall=0
        self.sumtotald=0
        self.sumtotall=0
        self.totall = MealInput.objects.aggregate(Sum('nurul'))
        self.totald= MealInput.objects.aggregate(Sum('nurud'))
        for self.j in self.totall.values():
           self.sumtotall= self.j
        for self.q in self.totald.values():
           self.sumtotald= self.q
        return self.sumtotald+self.sumtotall

    def abirmeal(self):  # this function is used for calculate the total meal of each person
        self.totald=0
        self.totall=0
        self.sumtotald=0
        self.sumtotall=0
        self.totall = MealInput.objects.aggregate(Sum('abirl'))
        self.totald= MealInput.objects.aggregate(Sum('abird'))
        for self.j in self.totall.values():
           self.sumtotall= self.j
        for self.q in self.totald.values():
           self.sumtotald= self.q
        return self.sumtotald+self.sumtotall

    def grandmeal(self):   # this function is used for to calculate the grand total(whole meal) of all persons
        self.membergrandmeal=MealInput.mehedimeal(self)+MealInput.omarmeal(self)+MealInput.shafinmeal(self)+MealInput.bikimeal(self)+MealInput.nurumeal(self)+MealInput.abirmeal(self)
        return self.membergrandmeal

# For meal rate calculation
    def mealrate(self):                 # self.mehedimeal is only perfect for MealInput model
        self.mealratio = 0.00           # MealInput.mehedimeal(self) can use anywhere
        self.tcost= Expense
        self.ttcost= self.tcost.totalcost(self) #(self) must use
        self.tmeal=MealInput.grandmeal(self)
        try:
            self.mealratio = self.ttcost / self.tmeal
        except:
            self.mealratio = 0
        return round(float(self.mealratio), 3)  # we used it to take upto 3 floating point


    def __str__(self):
        return str(self.date)




