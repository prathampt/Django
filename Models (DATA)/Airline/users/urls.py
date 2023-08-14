from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_views, name='login'),
    path('logout', views.logout_views, name='logout')
]