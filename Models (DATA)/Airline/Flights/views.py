from django.shortcuts import render

app_name = "Flights"

def index(request):
    return render(request, "Flights/index.html")
