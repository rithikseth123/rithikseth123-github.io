from django import forms
from .models import Product,ProductBuy



class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        exclude=["date","slug"]
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Assuming you have a field named 'name' that you want to use to generate the slug
        if 'name' in self.initial:
            self.fields['slug'].initial = self.initial['name']


class ProductBuyForm(forms.ModelForm):
    class Meta:
        model=ProductBuy
        fields="__all__"
