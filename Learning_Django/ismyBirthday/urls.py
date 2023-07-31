from django.urls import path
from . import views

app_name = "ismyBirthday"

urlpatterns = [
    path('', views.index, name='index'),
    path('parth/', views.index_p, name='parth_b-day'),
    path('today/', views.index_t, name='today')
]