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
            'date',
            'total_sales_amount',
            'total_profit_amount'
        ]
        widgets = {
            'invoice_code': forms.NumberInput(attrs={
                'placeholder': 'Code',
                'class': 'form-control'}),
            'date': forms.DateInput(attrs={
                'placeholder': 'Date',
                'class': 'form-control',
                'type': 'date'}),
            'total_sales_amount': forms.NumberInput(attrs={
                'placeholder': 'Total Montant Ventes',
                'class': 'form-control'}),
            'total_ptofit_amount': forms.NumberInput(attrs={
                'placeholder': 'Total Profuit Ventes',
                'class': 'form-control'})
        }


class InvoiceItemsForm(forms.ModelForm):

    class Meta:
        model = InvoiceItems
        fields = [
            'quantity',
            'unity_price',
            'total_price',
            'discount',
            'total_profit'
        ]
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'placeholder': 'Quantity',
                'class': 'form-control'}),
            'unity_price': forms.TextInput(attrs={
                'placeholder': 'Prix Unitaire',
                'class': 'form-control',
                'list': 'product_list'}),
            'total_price': forms.NumberInput(attrs={
                'placeholder': 'PR',
                'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={
                'placeholder': 'Marge',
                'class': 'form-control'}),
            'total_profit': forms.TextInput(attrs={
                'placeholder': 'Marge',
                'class': 'form-control'})
        }

    class Media(object):
        # The form must have `formset_media_js` in its Media
        js = formset_media_js + (
            # Other form javascript...
        )


InvoiceItemsFormSet = inlineformset_factory(
    Invoice, InvoiceItems, form=InvoiceItemsForm, can_delete=True, can_order=False, extra=1)
