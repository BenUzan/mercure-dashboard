from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    product_code = models.CharField(max_length=10)