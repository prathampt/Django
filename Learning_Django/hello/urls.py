from django.urls import path
from . import views

app_name = "hello"

urlpatterns = [
    path('', views.index, name='hello'),
    path('parth/', views.parth, name='parth'),
    path('<str:name>/', views.greet, name='greet')
]