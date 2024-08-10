import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from apps.sales.models import Invoice, Product
from apps.sales.forms import ProductForm, InvoiceForm, InvoiceItemsFormSet
from apps.sales.utils.code_generator import invoice_code_generator, product_code_generator
# Create your views here.


@login_required(login_url="/login")
def index(request):
    return render(request, 'sales\index.html')


def report(request):
    return render(request, "sales\\report.html")


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


def create_order(request):

    template = "sales\create_order.html"

    products = Product.objects.all

    formset = InvoiceItemsFormSet(request.POST or None)
    invoice_form = InvoiceForm(request.POST or None)

    if Invoice.objects.count() < 1:
        invoice_code = invoice_code_generator('')
    else:
        invoice = Invoice.objects.latest('invoice_code')
        invoice_code = invoice_code_generator(invoice.invoice_code)

    if request.method == 'POST':
        print('test')

        # * FIRST SAVE INVOICE
        if invoice_form.is_valid() and formset.is_valid():
            pass

        # * SECOND SAVE INVOICE ITEMS
        if formset.is_valid() and invoice_form.is_valid():

            final_formset = InvoiceItemsFormSet
            for form in formset:
                print(form.cleaned_data)

            final_formset.save()

    context = {"invoice_code": invoice_code,
               "product_list": products,
               "invoice_form": invoice_form,
               'formset': formset}

    return render(request, template, context)


def save_invoice(request):
    pass
