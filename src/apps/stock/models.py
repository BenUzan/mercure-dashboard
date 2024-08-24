from django.db import models

# Create your models here.


class purchase(models.Model):
    pass


class Stock(models.Model):
    product = models.OneToOneField(
        "sales.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    stock_min = models.IntegerField()
    stock_max = models.IntegerField()


class StockOut(models.Model):
    stock = models.ForeignKey(
        "stock.Stock", on_delete=models.CASCADE)
    product = models.ForeignKey("sales.Product", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    quantity = models.IntegerField()
    price_out = models.DecimalField(max_digits=5, decimal_places=2)


class StockIn(models.Model):
    supplier = models.ForeignKey("stock.Supplier", on_delete=models.CASCADE)
    product = models.ForeignKey("sales.Product", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    quantity = models.IntegerField()
    price_out = models.DecimalField(max_digits=5, decimal_places=2)


class Supplier(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    adress = models.TextField()
    email = models.EmailField(max_length=254)
    phone = models.TextField()
    pass
