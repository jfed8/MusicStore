from django.db import models
from polymorphic.models import PolymorphicModel


class Category(models.Model):
    #id
    codename = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Create your models here.
class Product(PolymorphicModel):
    #id
    name = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category')
    price = models.DecimalField(max_digits=8, decimal_places=2) # 999,999.00
    graphic = models.TextField(blank=True, null=True)
    available = models.BooleanField(default = 1)
    create_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now= True)

class ProductPicture(models.Model):
    product = models.ForeignKey('Product')
    path = models.TextField(blank=True, null=True)



class BulkProduct(Product):
    # Automatic: id, create_date, modified_date
    # name
    # category
    # price
    barcode = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    reorder_trigger = models.IntegerField()
    reorder_quantity = models.IntegerField()


class UniqueProduct(Product):
    # Automatic: id, create_date, modified_date
    # name
    # category
    # price
    serial_number = models.TextField(blank=True, null=True)
    condition = models.TextField(blank=True, null=True)




class RentalProduct(Product):
    # Automatic: id, create_date, modified_date
    # name
    # category
    # price
    serial_number = models.TextField(blank=True, null=True)
    is_rented = models.BooleanField() # 0 = No, 1 = Yes
    condition = models.TextField(blank=True, null=True) #New, Damaged, Used
    due_date = models.DateTimeField(blank=True, null=True)
