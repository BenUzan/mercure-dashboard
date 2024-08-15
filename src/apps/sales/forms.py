from django import forms
from django.forms import SelectDateWidget, formset_factory, modelformset_factory, inlineformset_factory
from apps.sales.models import Product, Invoice, InvoiceItems
from djangoformsetjs.utils import formset_media_js


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'price_achat',
            'price_revient',
            'marge',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Designation',
                'class': 'form-control',
                'id': 'floatingInput',
                'list': 'product-list'}),
            'price_achat': forms.TextInput(attrs={
                'placeholder': 'PA',
                'class': 'form-control',
                'id': 'floatingInput'}),
            'price_revient': forms.TextInput(attrs={
                'placeholder': 'PR',
                'class': 'form-control',
                'id': 'floatingInput'}),
            'marge': forms.TextInput(attrs={
                'placeholder': 'Marge',
                'class': 'form-control',
                'id': 'floatingInput'})
        }


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = [
            'invoice_code',
            'date'
            # 'total_sales_amount',
            # 'total_profit_amount'
        ]
        widgets = {
            'invoice_code': forms.TextInput(attrs={
                'placeholder': 'Code',
                'class': 'form-control',
                'disabled': 'disabled'}),
            'date': forms.DateInput(attrs={
                'placeholder': 'Date',
                'class': 'form-control',
                'type': 'date'})
            # 'total_sales_amount': forms.NumberInput(attrs={
            #     'placeholder': 'Total Montant Ventes',
            #     'class': 'form-control'}),
            # 'total_profit_amount': forms.NumberInput(attrs={
            #     'placeholder': 'Total Profit Ventes',
            #     'class': 'form-control'})
        }


class InvoiceItemsForm(forms.Form):

    product_code = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Code du produit',
            'class': 'form-control',
            'list': 'product_list',
            'required': 'true'}))

    quantity = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Quantity',
            'class': 'form-control input quantity',
            'min': 1,
            'required': 'true'}))

    unity_price = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Prix Unitaire',
            'class': 'form-control input prix_unitaire',
            'min': 1,
            'required': 'true'}))

    discount = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Reduction',
            'class': 'form-control input discount',
            'min': 0,
            'required': 'true'}))

    total_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Prix Total',
            'class': 'form-control input total_price',
            'disabled': 'disabled',
            'required': 'true'}))

    class Media(object):
        # The form must have `formset_media_js` in its Media
        js = formset_media_js + (
            # Other form javascript...
        )


InvoiceItemsFormSet = formset_factory(
    InvoiceItemsForm, can_delete=True, can_order=False, extra=1)


# class InvoiceItemsForm(forms.ModelForm):

#     class Meta:
#         model = InvoiceItems
#         fields = [
#             # 'product',
#             'quantity',
#             'unity_price',
#             'discount',
#             'total_price'
#             # 'total_profit'
#         ]
#         widgets = {
#             # 'product': forms.TextInput(attrs={
#             #     'placeholder': 'Code du produit',
#             #     'class': 'form-control',
#             #     'list': 'product_list'}),
#             'quantity': forms.NumberInput(attrs={
#                 'placeholder': 'Quantity',
#                 'class': 'form-control input quantity'}),
#             'unity_price': forms.NumberInput(attrs={
#                 'placeholder': 'Prix Unitaire',
#                 'class': 'form-control input prix_unitaire'}),
#             'discount': forms.NumberInput(attrs={
#                 'placeholder': 'Reduction',
#                 'class': 'form-control'}),
#             'total_price': forms.NumberInput(attrs={
#                 'placeholder': 'Prix Total',
#                 'class': 'form-control input pt'})
#             # 'total_profit': forms.TextInput(attrs={
#             #     'placeholder': 'Prix total',
#             #     'class': 'form-control',
#             #     'disabled': 'disabled'})
#         }

#     class Media(object):
#         # The form must have `formset_media_js` in its Media
#         js = formset_media_js + (
#             # Other form javascript...
#         )


# InvoiceItemsFormSet = formset_factory(
#     InvoiceItemsForm, can_delete=True, can_order=False, extra=1)
