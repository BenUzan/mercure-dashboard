from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ProfilUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # phone_number = ...
    email = models.EmailField(help_text="L'adresse mail")
    username = models.CharField(max_length=50, help_text="Le pseudo")
    password = models.CharField(max_length=16, help_text="Le mdp")
    is_livreur = models.BooleanField(default=True)
