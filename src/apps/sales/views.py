import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from apps.sales.models import Product
from apps.sales.forms import ProductForm, InvoiceItemsFormSet

# Create your views here.


@login_required(login_url="/login")
def index(request):
    return render(request, 'sales\index.html')


def report(request):
    return render(request, "sales\\report.html")

# * Methode for geneate product code with the last
# * record in product table


def product_code_generator(product_code):
    product_code_prefix = 'ART-'
    product_code_suffix = ["-", "-0", "-00", "-000", "-0000"]

    # Extraction of the 6 latest charcater form product_code
    product_code = product_code[-6:]

    new_product_code = 0

    # loop for extract number from product_code
    for i in range(len(product_code_suffix)):
        x = re.split(product_code_suffix[i], product_code)
        print(x)

        try:
            if int(x[1]):
                new_product_code = int(x[1]) + 1
        except:
            pass

    if new_product_code == 0:  # create a new and the first product_code for the Table
        new_product_code = 'ART-00001'
    else:  # create a new product_code for the Table
        new_product_code = str(new_product_code)
        for x in range(5):
            if len(new_product_code) < 5:
                new_product_code = f'0{new_product_code}'
            else:
                new_product_code = f'{product_code_prefix}{new_product_code}'

    return new_product_code


def create_product(request):
    template = "sales\create_product.html"

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            if Product.objects.count() < 1:
                product_code = product_code_generator('')
            else:
                product = Product.objects.latest('product_code')
                product_code = product_code_generator(product.product_code)

            price_achat = form.cleaned_data['price_achat']
            price_revient = form.cleaned_data['price_revient']
            marge = form.cleaned_data['marge']
            price_ventes = (price_achat + price_revient) + marge
            benefice = price_ventes - (price_achat + price_revient)
            prod = Product(
                name=name,
                product_code=product_code,
                price_achat=price_achat,
                price_revient=price_revient,
                marge=marge,
                price_ventes=price_ventes,
                benefice=benefice
            )

            prod.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, template, {"form": form})


def update_product(request, id):
    template = "sales\\update_product.html"
    product = Product.objects.get(id=id)

    return render(request, template, {"product": product})


def update_product_record(request, id):

    if request.method == 'POST':

        name = request.POST['name']
        product_code = request.POST['product_code']
        price_achat = float(request.POST['price_achat'])
        price_revient = float(request.POST['price_revient'])
        marge = float(request.POST['marge'])

        price_ventes = (price_achat + price_revient) + marge
        benefice = price_ventes - (price_achat + price_revient)

        product = Product.objects.get(id=id)

        product.product_code = product_code
        product.name = name
        product.price_achat = price_achat
        product.price_revient = price_revient
        product.marge = marge
        product.price_ventes = price_ventes
        product.benefice = benefice

        product.save()

    return redirect("product_list")


def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()

    return redirect("product_list")


def product_list(request):
    products = Product.objects.all()
    template = "sales\product_list.html"

    return render(request, template, {"products": products})


item = []


def create_order(request):
    template = "sales\create_order.html"
    products = Product.objects.all
    formset = InvoiceItemsFormSet(request.POST or None)

    if request.method == 'POST':
        print('test')
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)

    return render(request, template, {"item_list": item, "product_list": products, 'formset': formset})


def save_invoice(request):
    pass
