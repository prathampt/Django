from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parth/', views.index_p, name='parth_b-day'),
    path('today/', views.index_t, name='today')
]