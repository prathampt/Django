from django.shortcuts import render

from .models import flight

app_name = "Flights"

def index(request):
    return render(request, "Flights/index.html",{
        "flights": flight.objects.all()
    })

def Flight(request, flight_id):
    Flight = flight.objects.get(id=flight_id)
    return render(request, "Flights/flight.html", {
        "flight": Flight,
        "passangers": Flight.passangers.all()
    })
