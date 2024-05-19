from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.index, name='homepage'),
    path('rapport/', views.rapport, name='rapport'),
]
