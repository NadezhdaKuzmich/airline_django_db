from django.shortcuts import render
from .models import Flight


def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    current_flight = Flight.objects.get(pk=flight_id)

    return render(request, "flights/flight.html", {
        "flight": current_flight,
        "passengers": current_flight.passengers.all()
    })
