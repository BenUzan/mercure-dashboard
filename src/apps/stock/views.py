from django.shortcuts import render
from apps.sales.models import Product
# Create your views here.


def stock_product_list(request):
    products = Product.objects.all()
    template = "stock\stock_product_list.html"

    return render(request, template, {"products": products})


def stock_product_mgmt(request, id=None):
    product = Product.objects.get(id=id)
    template = "stock\\stock_product_mgmt.html"

    return render(request, template)
