from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:flight_id>", views.Flight, name="flight"),
    path("<int:flight_id>/book", views.Book, name="book")
]