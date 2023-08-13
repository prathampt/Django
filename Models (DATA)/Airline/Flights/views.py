from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import flight,passanger

app_name = "Flights"

def index(request):
    return render(request, "Flights/index.html",{
        "flights": flight.objects.all()
    })

def Flight(request, flight_id):
    Flight = flight.objects.get(id=flight_id)
    return render(request, "Flights/flight.html", {
        "flight": Flight,
        "passangers": Flight.passangers.all(),
        "non_passangers": passanger.objects.exclude(flight=Flight).all()
    })

def Book(request, flight_id):
    if request.method == "POST":
        Flight = flight.objects.get(id=flight_id)
        Passanger = passanger.objects.get(pk=int(request.POST["passanger"]))
        Passanger.flight.add(Flight)
        return HttpResponseRedirect(reverse('flight',args=(flight_id,)))


