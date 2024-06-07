from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rapport/', views.rapport, name='rapport'),
]
