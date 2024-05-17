from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage', views.index),
    path('rapport', views.rapport, name='rapport'),
]
