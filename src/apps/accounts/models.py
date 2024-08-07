from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # phone_number = ...
    email = models.EmailField(help_text="L'adresse mail")
    username = models.CharField(max_length=50, help_text="Le pseudo")
    password = models.CharField(max_length=16, help_text="Le mdp")
