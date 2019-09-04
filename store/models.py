from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'store'



class Product(models.Model):
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50,unique=True)
    inventory_created_time = models.DateField()
    inventory_updated_time = models.DateField()
    class Meta:
        db_table = 'product'

class StoreStock(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory_quantity = models.IntegerField()
    inventory_created_time = models.DateField()
    inventory_updated_time = models.DateField()
    class Meta:
        db_table = 'store_stock'
        unique_together = [['store', 'product']]