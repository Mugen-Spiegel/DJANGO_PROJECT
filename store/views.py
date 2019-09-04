import json
import validators
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Store, Product, StoreStock
from .validator.validator import StoreParam, ProductParam, StoreStockParam, AddStoreProduct, StoreProduct
from django.core.exceptions import ValidationError
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.


@api_view(['POST'])
def store(requests):
    """
    This function is to add new store with url
    """
    param = requests.POST
    valid = StoreParam(param)
    response = HttpResponse({})

    if not "{}" == valid.errors.as_json():
        response = res(json.dumps({"message": valid.errors}), 422)
    else:
        valid = validators.url(param['url'])
        if not valid:
            error = json.dumps({"message": ["invalid URL"]})
            response = res(error,422) 
        else:
            try:
                storeModel = Store(name=param['name'], url = param['url'])
                if not storeModel.validate_unique():
                    storeModel.save()
                    response = res(json.dumps({"message": ["new store has been added"]}),200) 
            except ValidationError as e:
                response = res(json.dumps({"message": e.message_dict}),422)
    return response



@transaction.atomic
@api_view(['GET', 'POST'])
def products(requests):
    """
    POST method => This function is to add new product in store
    GET method => This function is to get all the product that store has
    """
    response = HttpResponse({})
    if requests.method == "POST":
        param = requests.POST
        valid = ProductParam(param)
        
        if not "{}" == valid.errors.as_json():
            response = res(json.dumps({"message": valid.errors}), 422)
        else:
            try:
                ProductModel = Product(name=param['name'],
                sku=param['sku'],
                inventory_created_time=param['created_at'],
                inventory_updated_time=param['updated_at']
                )
                
                if not ProductModel.validate_unique():
                    ProductModel.save()
                    StoreStockModel = StoreStock(product=Product.objects.get(id=ProductModel.id),
                    store=Store.objects.get(id=param['store_id']),
                    inventory_quantity=param['quantity'],
                    inventory_created_time=param['created_at'],
                    inventory_updated_time=param['updated_at'])
                    if not StoreStockModel.validate_unique():
                        StoreStockModel.save()
                        response = res(json.dumps({"message": ["product has been added "]}),200)

            except ValidationError as e:
                transaction.set_rollback(True)
                response = res(json.dumps({"message":e.message_dict}),422)
            except ObjectDoesNotExist as e:
                transaction.set_rollback(True)
                response = res(json.dumps({"message": ["Store not exist"]}),422)
    elif requests.method == "GET":
        param = requests.GET
        valid = StoreProduct(param)
        if not "{}" == valid.errors.as_json():
            response = res(json.dumps({"message": valid.errors}), 422)
        else:
            storeProd = StoreStock.objects.select_related('store', 'product') \
            .values('store__id', 'store__name','product__id', 'product__name', 'product__sku', 'inventory_quantity', \
            'inventory_updated_time').filter(store=param['store_id'])
            data = list(storeProd)
            response = res(json.dumps({"data": data},cls=DjangoJSONEncoder),200)

    return response

@api_view(['GET'])
def storeProdAvailability(request,store_id,product_id):
    """
    This function is to get the specific product of the store
    """
    response = HttpResponse({})
    storeProd = StoreStock.objects.select_related('store', 'product') \
        .values('store__id', 'store__name', 'product__id', 'product__name', 'product__sku', 'inventory_quantity', \
        'inventory_updated_time').filter(store=store_id, product=product_id)
    data = list(storeProd)
    print(storeProd,store_id,product_id)
    response = res(json.dumps({"data": data},cls=DjangoJSONEncoder),200)
    return response

@api_view(['POST'])
def updateStoreStock(requests):
    """
    This function is to update the specific product of store
    """
    response = HttpResponse({})
    param = requests.POST
    valid = StoreStockParam(param)
    if not "{}" == valid.errors.as_json():
        response = res(json.dumps({"message": valid.errors}), 422)
    else:
        try:
            storeProd = StoreStock.objects.filter(store=param["store_id"], product=param["product_id"]).update(inventory_quantity=param["quantity"],
            inventory_updated_time=param["updated_at"])
            response = res(json.dumps({"message": ["Stock Quantity Updated!"]}), 200)
        except ValidationError as e:
            response = res(json.dumps({"message": e.message_dict}),422)
    return response


@transaction.atomic
@api_view(['POST'])
def addStoreProductStock(requests):
    """
    This function is to add existing product in existing store
    """
    response = HttpResponse({})
    param = requests.POST
    valid = AddStoreProduct(param)
    if not "{}" == valid.errors.as_json():
        response = res(json.dumps({"message": valid.errors}), 422)
    else:
        try:
            print(param['product_id'])
            StoreStockModel = StoreStock(product=Product.objects.get(id=param['product_id']),
                    store=Store.objects.get(id=param['store_id']),
                    inventory_quantity=param['quantity'],
                    inventory_created_time=param['created_at'],
                    inventory_updated_time=param['created_at'])
            if not StoreStockModel.validate_unique():
                        StoreStockModel.save()
                        response = res(json.dumps({"message": ["product has been added "]}),200)
        except ValidationError as e:
            transaction.set_rollback(True)
            response = res(json.dumps({"message": e.message_dict}),422)
        except Product.DoesNotExist as e:
                transaction.set_rollback(True)
                response = res(json.dumps({"message":["Product Does not exist"]}),422)
        except Store.DoesNotExist as e:
                transaction.set_rollback(True)
                response = res(json.dumps({"message":["Store Does not exist"]}),422)
    return response


def res(e, code):
    
    res = HttpResponse(e, content_type="application/json")
    res.status_code = code
    return res