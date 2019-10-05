from django.shortcuts import render,redirect
from deposit.models import Deposit
# How to insert data into a database from an HTML form in Django
def depositview(request):
    if request.method == 'POST':
        if request.POST.get('mdepo') or request.POST.get('odepo')\
                or request.POST.get('sdepo') or  request.POST.get('bdepo') or  request.POST.get('ndepo') \
                or  request.POST.get('adepo'):
            costs = Deposit()


            costs.mehedidepo = request.POST.get('mdepo')
            costs.omardepo = request.POST.get('odepo')

            costs.shafindepo= request.POST.get('sdepo')

            costs.bikidepo= request.POST.get('bdepo')

            costs.nurudepo= request.POST.get('ndepo')

            costs.abirdepo= request.POST.get('adepo')
            costs.save()

            return redirect('deposit')
    else:
        return render(request, 'deposit.html')