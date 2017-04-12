# ACCOUNT MODELS
from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog import models as cmod
from checkout import models as checkmod
from decimal import Decimal

# Define models here

CONTACT_CHOICES = [
    ['text', 'Text'],
    ['email', 'Email'],
    ['voice', 'Voice'],
]

GENDER_CHOICES = [
    ['M', 'Male'],
    ['F', 'Female'],
    ['other', 'Other'],
]

class FOMOUser(AbstractUser):
    #password
    #last_login
    #username
    #first_name
    #last_name
    #email
    #is_staff
    #is_active
    #date_joined

    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zipcode = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    pref_contact = models.TextField(null=True, blank=True, choices = CONTACT_CHOICES)
    birthday = models.DateField(null=True, blank=True)
    gender = models.TextField(null=True, blank=True, choices = GENDER_CHOICES)

    def displayHistory(self):
        userhistory = HistoryItem.objects.filter(FOMOUser_id = self.id)
        historyitems = []
        for line in userhistory:
            try:
                product = cmod.Product.objects.get(id = line.product_id)
                if product in historyitems: #if already in the list, move to the top
                    position = historyitems.index(product)
                    historyitems.insert(0, historyitems.pop(position))
                else: #else, simply add to top of list
                    historyitems.insert(0, product)
            except cmod.Product.DoesNotExist:
                print('Product no longer available')
        return historyitems[:5]

    def retrieveCart(self):
        usercart = CartItem.objects.filter(FOMOUser_id = self.id, status = 'active')
        return usercart

    def retrieveOrders(self):
        orders = checkmod.Sale.objects.filter(FOMOUser_id = self.id)
        return orders

    def emptyCart(self):
        for item in self.retrieveCart():
            item.status = 'removed'
            item.save()

    def get_cart_count(self):
        usercart = CartItem.objects.filter(FOMOUser_id = self.id, status = 'active')
        return len(usercart)

    def cartSubtotal(self):
        usercart = CartItem.objects.filter(FOMOUser_id = self.id, status = 'active')
        subtotal = Decimal('0.00')
        for item in usercart:
            subtotal += item.ext_price
        return subtotal

    def cartTax(self):
        TAX_RATE = Decimal('.0725')
        subtotal = self.cartSubtotal()
        tax = Decimal('0.00')
        tax = subtotal * TAX_RATE
        return round(tax, 2)

    def cartShipping(self):
        shipping = Decimal('10.00')
        return shipping

    def cartTotal(self):
        total = self.cartSubtotal()
        total += self.cartTax()
        total += self.cartShipping()
        return total

Status_HistoryItem = [
    ['viewed', 'Viewed'],
    ['cartitem', 'CartItem'],
]

class HistoryItem(models.Model):
    #id
    FOMOUser = models.ForeignKey('FOMOUser', related_name = 'history')
    product = models.ForeignKey('catalog.Product')
    date_stamp = models.DateTimeField(auto_now= True)
    status = models.TextField(null=True, blank=True, choices = Status_HistoryItem, default='viewed')

Status_CartItem = [
    ['active', 'Active'],
    ['purchased', 'Purchased'],
    ['removed', 'Removed'],
]

class CartItem(models.Model):
    #id
    FOMOUser = models.ForeignKey('FOMOUser', related_name = 'cart')
    product = models.ForeignKey('catalog.Product')
    date_stamp = models.DateTimeField(auto_now= True)
    quantity = models.IntegerField()
    ext_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.TextField(null=True, blank=True, choices = Status_CartItem, default='active')

    def removeItem(self):
        self.status = 'removed'
        self.save()
