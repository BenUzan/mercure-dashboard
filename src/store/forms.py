from django import forms
from django.forms import modelformset_factory
from store.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "price_achat",
            "price_revient",
            "marge",
        ]
        widgets = {
            "name": forms.TextInput(attrs={
                'placeholder': 'Designation',
                'class': 'form-control',
                'id': 'floatingInput'}),
            "price_achat": forms.TextInput(attrs={
                'placeholder': 'PA',
                'class': 'form-control',
                'id': 'floatingInput'}),
            "price_revient": forms.TextInput(attrs={
                'placeholder': 'PR',
                'class': 'form-control',
                'id': 'floatingInput'}),
            "marge": forms.TextInput(attrs={
                'placeholder': 'Marge',
                'class': 'form-control',
                'id': 'floatingInput'})
        }
