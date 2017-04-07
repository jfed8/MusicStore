from django.db import models
from decimal import Decimal
from catalog import models as cmod


# Create your models here.
class ShippingAddress(models.Model):
    FOMOUser = models.ForeignKey('account.FOMOUser', related_name = 'shippingaddress')
    fullname = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zipcode = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)

class Sale(models.Model):
    #id
    FOMOUser = models.ForeignKey('account.FOMOUser', related_name = 'sale')
    ship_address = models.ForeignKey('ShippingAddress', related_name = 'ship_address')
    date_stamp = models.DateTimeField(auto_now= True)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    tax = models.DecimalField(max_digits=8, decimal_places=2)
    shipping = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)


    @staticmethod
    def record_sale(user, usercart, cart_subtotal, cart_tax, cart_shipping, cart_total, ship_address, stripe_charge):
        print('>>>>>>>>>>>>>>>>>>>>>>>>record_sale')
        sale = Sale()
        sale.FOMOUser = user
        sale.ship_address = ship_address
        sale.subtotal = cart_subtotal
        sale.tax = cart_tax
        sale.shipping = cart_shipping
        sale.total = cart_total
        sale.save()

        for item in usercart:
            saleitem = SaleItem()
            saleitem.sale = sale
            saleitem.product = item.product
            saleitem.quantity = item.quantity
            saleitem.sale_price = item.ext_price
            saleitem.save()

            product = cmod.Product.objects.get(id=item.product.id)
            if hasattr(product, 'quantity'):
                product.quantity = product.quantity - saleitem.quantity
                if product.quantity <= 0:
                    product.available = False
            else:
                product.available = False
            product.save()

        payment = Payment()
        payment.sale = sale
        payment.stripe_chargeid = stripe_charge.id
        payment.amount = Decimal(stripe_charge.amount) / Decimal('100')
        payment.amount_refunded = stripe_charge.amount_refunded
        payment.currency = stripe_charge.currency
        payment.description = stripe_charge.description
        payment.paid = stripe_charge.paid
        payment.card_brand = stripe_charge.source.brand
        payment.method = stripe_charge.source.funding + ' ' + stripe_charge.source.object
        payment.card_expiration = str(stripe_charge.source.exp_month) + '/' + str(stripe_charge.source.exp_year)
        payment.save()

        return sale

class SaleItem(models.Model):
    sale = models.ForeignKey('Sale', related_name = 'saleitem')
    product = models.ForeignKey('catalog.Product')
    quantity = models.IntegerField()
    sale_price = models.DecimalField(max_digits=8, decimal_places=2)



class Payment(models.Model):
    sale = models.ForeignKey('Sale', related_name = 'salepayment')
    stripe_chargeid = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    amount_refunded = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    paid = models.BooleanField()
    method = models.TextField(null=True, blank=True)
    card_brand = models.TextField(null=True, blank=True)
    card_expiration = models.TextField(null=True, blank=True)
