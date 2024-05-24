from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(help_text="L'adresse mail")
    pseudo = models.CharField(max_length=50, help_text="Le pseudo")
    password = models.CharField(max_length=16, help_text="Le mdp")