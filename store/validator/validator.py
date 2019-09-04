from django import forms
from ..models import Product, StoreStock
class StoreParam(forms.Form):

    name = forms.CharField(max_length=50, min_length=5, error_messages={
        'required': 'name must be provide',
        'max_length': 'Max length 50',
    })
    
    url = forms.CharField(max_length=50, min_length=11, error_messages={
        'required': 'url must be provide',
        'max_length': 'Max length 50',
        'min_length': 'Max length 11',
    })


class ProductParam(forms.Form):

    name = forms.CharField(required=True)
    sku = forms.CharField(required=True)
    quantity = forms.IntegerField(required=True, min_value=1)
    store_id = forms.IntegerField(required=True)
    created_at = forms.DateField(required=True, input_formats=['%Y-%m-%d'])
    updated_at = forms.DateField(required=True, input_formats=['%Y-%m-%d'])
    class Meta:
        model = Product
        exclude = ('inventory_created_time')

class StoreProduct(forms.Form):
    store_id = forms.IntegerField(required=True)

class StoreStockParam(forms.Form):

    store_id = forms.IntegerField(required=True)
    product_id = forms.IntegerField(required=True)
    quantity = forms.IntegerField(required=True)
    updated_at = forms.DateField(required=True, input_formats=['%Y-%m-%d'])
    class Meta:
        model = StoreStock
        exclude = ('inventory_created_time')

class AddStoreProduct(forms.Form):

    quantity = forms.IntegerField(required=True, min_value=1)
    store_id = forms.IntegerField(required=True)
    product_id = forms.IntegerField(required=True)
    created_at = forms.DateField(required=True, input_formats=['%Y-%m-%d'])
