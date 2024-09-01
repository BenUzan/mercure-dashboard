from django.db import models
from django.forms import model_to_dict
from django.urls import reverse


from django_extensions.db.fields import AutoSlugField

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


class Sale(models.Model):
    """
    Represents a sale transaction involving a customer.
    """

    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Sale Date"
    )
    sub_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    tax_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    tax_percentage = models.FloatField(default=0.0)
    amount_paid = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    amount_change = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )

    class Meta:
        db_table = "sales"
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        """
        Returns a string representation of the Sale instance.
        """
        return (
            f"Sale ID: {self.id} | "
            f"Grand Total: {self.grand_total} | "
            f"Date: {self.date_added}"
        )

    def sum_products(self):
        """
        Returns the total quantity of products in the sale.
        """
        return sum(detail.quantity for detail in self.saledetail_set.all())

class Item(models.Model):
    """
    Represents an item in the inventory.
    """
    slug = AutoSlugField(unique=True, populate_from='name')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    expiring_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """
        String representation of the item.
        """
        return (
            f"{self.name} - Category: {self.category}, "
            f"Quantity: {self.quantity}"
        )

    def get_absolute_url(self):
        """
        Returns the absolute URL for an item detail view.
        """
        return reverse('item-detail', kwargs={'slug': self.slug})

    def to_json(self):
        product = model_to_dict(self)
        product['id'] = self.id
        product['text'] = self.name
        product['category'] = self.category.name
        product['quantity'] = 1
        product['total_product'] = 0
        return product

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Items'
        
class SaleDetail(models.Model):
    """
    Represents details of a specific sale, including item and quantity.
    """

    sale = models.ForeignKey(
        "stock.Sale",
        on_delete=models.CASCADE,
        db_column="sale",
        related_name="saledetail_set"
    )
    item = models.ForeignKey(
        "stock.Item",
        on_delete=models.DO_NOTHING,
        db_column="item"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField()
    total_detail = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "sale_details"
        verbose_name = "Sale Detail"
        verbose_name_plural = "Sale Details"

    def __str__(self):
        """
        Returns a string representation of the SaleDetail instance.
        """
        return (
            f"Detail ID: {self.id} | "
            f"Sale ID: {self.sale.id} | "
            f"Quantity: {self.quantity}"
        )


