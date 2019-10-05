from django.shortcuts import render,redirect
from mealinput.models import MealInput
# How to insert data into a database from an HTML form in Django
def mealinputformview(request):
    if request.method == 'POST':
        if request.POST.get('date') \
                and request.POST.get('ml') and request.POST.get('md')\
                and request.POST.get('ol') and request.POST.get('od')\
                and request.POST.get('sl') and request.POST.get('sd') \
                and request.POST.get('bl') and request.POST.get('bd') \
                and request.POST.get('nl') and request.POST.get('nd') \
                and request.POST.get('al') and request.POST.get('ad'):
            meal = MealInput()
            meal.date = request.POST.get('date')
            meal.mehedil = request.POST.get('ml')
            meal.mehedid = request.POST.get('md')
            meal.omarl = request.POST.get('ol')
            meal.omard = request.POST.get('od')
            meal.shafinl = request.POST.get('sl')
            meal.shafind = request.POST.get('sd')
            meal.bikil = request.POST.get('bl')
            meal.bikid = request.POST.get('bd')
            meal.nurul = request.POST.get('nl')
            meal.nurud = request.POST.get('nd')
            meal.abirl = request.POST.get('al')
            meal.abird = request.POST.get('ad')

            meal.save()
            return redirect('mealinput')
    else:
        return render(request, 'mealinput.html')