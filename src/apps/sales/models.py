from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=50)
    localistation = models.CharField(max_length=50)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)


class Product(models.Model):
    name = models.CharField(max_length=50)  # ! La taille A revoir !!!
    product_code = models.CharField(max_length=100)  # ! La taille a revoir !!!
    price_achat = models.DecimalField(max_digits=18, decimal_places=2)
    price_revient = models.DecimalField(max_digits=18, decimal_places=2)
    marge = models.DecimalField(max_digits=18, decimal_places=2)
    price_ventes = models.DecimalField(max_digits=18, decimal_places=2)
    benefice = models.DecimalField(max_digits=18, decimal_places=2)

    # def __str__(self):
    #     field_values = []
    #     for field in self._meta.get_fields():
    #         field_values.append(str(getattr(self, field.name, '')))
    #     return ' '.join(field_values)


class StockProduct(models.Model):
    fk_product_code = models.CharField(max_length=10)
    quantity = models.IntegerField()

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)


class Invoice(models.Model):
    invoice_code = models.CharField(max_length=10)
    date = models.DateField()
    total_sales_amount = models.DecimalField(
        max_digits=18, decimal_places=2, blank=True, null=True)
    total_profit_amount = models.DecimalField(
        max_digits=18, decimal_places=2, blank=True, null=True)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)


class InvoiceItems(models.Model):
    invoice = models.ForeignKey(
        "sales.Invoice", on_delete=models.CASCADE)
    product = models.ForeignKey(
        "sales.Product", on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=18, decimal_places=2)
    unity_price = models.DecimalField(max_digits=18, decimal_places=2)
    total_price = models.DecimalField(max_digits=18, decimal_places=2)
    discount = models.DecimalField(max_digits=18, decimal_places=2)
    total_profit = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)


class Report(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # user_id = models.ForeignKey(
    #  "store.Model", verbose_name=(""), on_delete=models.CASCADE)
