import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from apps.sales.models import InvoiceItems, Invoice, Product
from apps.sales.forms import ProductForm, InvoiceForm, InvoiceItemsFormSet
from apps.sales.utils.code_generator import invoice_code_generator, product_code_generator

import pdfkit
from pypdf import PdfReader, PdfWriter
# Create your views here.


@login_required(login_url="/login")
def delivery(request):
    return render(request, 'sales\delivery.html')


def report_list(request):
    template = "sales\\report_list.html"

    invoices = Invoice.objects.all()

    context = {
        'invoices': invoices}
    return render(request, template, context)


def report_details(request, id=None):
    invoice = get_object_or_404(Invoice, id=id)
    invoiceitem = invoice.invoiceitems_set.all()

    # Calcule du prix de revient total

    # Calcule de la marge total

    # Calcule de la difference et des differentes peertes

    context = {
        "company": {
            "name": "MERCURE 1",
            "address": "1B Lubumbashi, RDC",
            "phone": "(243) XXX XXXX",
            "email": "uzanmuyumbaben@gmial.com",
        },
        "invoice_id": invoice.id,
        "invoice_total": invoice.total_sales_amount,
        "customer": 'Maitre Olivier',
        "customer_email": '@gmail.com',
        "date": invoice.date,
        "due_date": invoice.date,
        "billing_address": 'Lubumbashi, Haut-Katanga',
        "message": 'Bon',
        "invoiceitem": invoiceitem,

    }
    return render(request, 'sales/report_details.html', context)


# todo : rapport detailee
def extra_report_details(request, id=None):
    invoice = get_object_or_404(Invoice, id=id)

    invoiceitem = invoice.invoiceitems_set.all()

    # Calcule du prix de revient total

    # Calcule de la marge total
    for keys, item in enumerate(invoiceitem):
        print(keys)
        print(item)

    # Calcule de la difference et des differentes peertes

    context = {
        "company": {
            "name": "MERCURE 1",
            "address": "1B Lubumbashi, RDC",
            "phone": "(243) XXX XXXX",
            "email": "uzanmuyumbaben@gmial.com",
        },
        "invoice_id": invoice.id,
        "invoice_total": invoice.total_sales_amount,
        "customer": 'Maitre Olivier',
        "customer_email": '@gmail.com',
        "date": invoice.date,
        "due_date": invoice.date,
        "billing_address": 'Lubumbashi, Haut-Katanga',
        "message": 'Bon',
        "invoiceitem": invoiceitem,

    }
    return render(request, 'sales/extra_report_details.html', context)


def generate_report(request, id=None):

    invoice = Invoice.objects.get(id=id)
    invoice_code = invoice.invoice_code

    print(invoice_code)

    # Use False instead of output path to save pdf to a variable
    # by using configuration you can add path value.
    wkhtml_path = pdfkit.configuration(
        wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

    pdf = pdfkit.from_url(request.build_absolute_uri(
        reverse('report-details', args=[id])), False, configuration=wkhtml_path)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice-{invoice_code}.pdf"'

    # reader = PdfReader(f"C:/Users/SK/Downloads/invoice-{invoice_code}.pdf")
    # writer = PdfWriter()

    # writer.append_pages_from_reader(reader)
    # writer.encrypt("rootroot")

    # with open("C:/Users/SK/Downloads/output.pdf", "wb") as out_file:
    #     writer.write(out_file)

    return response
    # return render(request, "sales\\report.html")


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

    # Generation du nemero du rapport
    if Invoice.objects.count() < 1:
        invoice_code = invoice_code_generator('')
    else:
        invoice = Invoice.objects.latest('invoice_code')
        invoice_code = invoice_code_generator(invoice.invoice_code)

    if request.method == 'POST':

        invoice_form = InvoiceForm(request.POST or None, initial={
            'invoice_code': invoice_code})
        formset = InvoiceItemsFormSet(request.POST or None)

        # * FIRST SAVE INVOICE
        if invoice_form.is_valid():
            print('test')
            fac = invoice_form.cleaned_data.get('invoice_code')
            date = invoice_form.cleaned_data.get('date')

            tsm = 0
            tpf = 0

            invoice = Invoice.objects.create(
                invoice_code=fac,
                date=date,
            )

        # * SECOND SAVE INVOICE ITEMS
        if formset.is_valid():
            print('test')
            # final_formset = InvoiceItemsFormSet

            total_sales_amount = 0
            total_profit_amount = 0

            for form in formset:

                delete = form.cleaned_data.get('DELETE')

                if delete:
                    continue

                prod = form.cleaned_data.get('product_code')

                try:
                    product_instance = Product.objects.get(product_code=prod)
                except:
                    #! doit envoyer un message derruer
                    product_instance = None

                quantity = form.cleaned_data.get('quantity')
                unity_price = form.cleaned_data.get('unity_price')
                discount = form.cleaned_data.get('discount')
                total_price = form.cleaned_data.get('total_price')

                total_profit = product_instance.benefice

                if not delete:
                    total_profit = total_profit * quantity
                    total_sales_amount += total_price
                    total_profit_amount += total_profit

                    InvoiceItems(
                        invoice=invoice,
                        product=product_instance,
                        quantity=quantity,
                        unity_price=unity_price,
                        total_price=total_price,
                        discount=discount,
                        total_profit=total_profit
                    ).save()

            invoice.total_sales_amount = total_sales_amount
            invoice.total_profit_amount = total_profit_amount
            invoice.save()

            return redirect('report-list')
        #     final_formset.save()
    else:
        formset = InvoiceItemsFormSet(request.POST or None)
        invoice_form = InvoiceForm(request.POST or None, initial={
                                   'invoice_code': invoice_code})

    context = {"invoice_code": invoice_code,
               "product_list": products,
               "invoice_form": invoice_form,
               'formset': formset}

    return render(request, template, context)


def save_invoice(request):
    pass
