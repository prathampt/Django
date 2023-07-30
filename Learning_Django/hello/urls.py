from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='hello'),
    path('parth/', views.parth, name='parth'),
    path('<str:name>/', views.greet, name='greet')
]