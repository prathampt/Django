from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createnew/", views.createNew, name="createNew"),
    path("<str:title>/", views.entryTitle, name="title")
]
