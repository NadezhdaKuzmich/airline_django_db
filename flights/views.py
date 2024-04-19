from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger


def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    current_flight = Flight.objects.get(pk=flight_id)

    return render(request, "flights/flight.html", {
        "flight": current_flight,
        "passengers": current_flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=current_flight).all()
    })


def book(request, flight_id):
    if request.method == "POST":
        current_flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(current_flight)
        return HttpResponseRedirect(
            reverse("flight", args=(current_flight.id,)))
