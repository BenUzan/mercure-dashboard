from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signupaccount, name="signup"),
    path("login/", views.loginaccount, name="login"),
    path("logout/", views.logoutaccount, name="logout")
    
]
