from django.urls import path

from apps.dashboard import views


urlpatterns = [
    path('', views.start, name="start"),
    path("dashboard", views.dashboard, name="dashboard")
]
