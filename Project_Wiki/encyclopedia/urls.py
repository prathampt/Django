from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createnew/", views.createNew, name="createNew"),
    path("<str:title>/", views.entryTitle, name="title"),
    path("<str:title>/edit", views.edit, name="edit"),
    path("random", views.Random, name="random")
]
