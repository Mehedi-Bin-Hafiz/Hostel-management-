from django.shortcuts import render,redirect
from dailyexpense.models import Expense
# How to insert data into a database from an HTML form in Django
def expenseformview(request):
    if request.method == 'POST':
        if request.POST.get('exdate') \
                and request.POST.get('cost'):
            costs = Expense()
            costs.exdate = request.POST.get('exdate')
            costs.cost = request.POST.get('cost')

            costs.save()
            return redirect('dailyexpense')
    else:
        return render(request, 'DailyExpense.html')