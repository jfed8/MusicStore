from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from account import models as amod
from catalog import models as cmod
from checkout import models as checkmod
from formlib.form import FormMixIn
from django.http import HttpResponseRedirect
from django import forms
import stripe
from decimal import Decimal

from .. import dmp_render, dmp_render_to_string

@view_function
@login_required(login_url='/account/login/')
def process_request(request):
    usercart = request.user.retrieveCart()

    # Redirect if cart is empty
    if len(usercart) <= 0:
        return HttpResponseRedirect('/catalog/')

    cart_subtotal = request.user.cartSubtotal()
    cart_tax = request.user.cartTax()
    cart_shipping = request.user.cartShipping()
    cart_total = request.user.cartTotal()
    try:
        ship_address = checkmod.ShippingAddress.objects.get(id=request.urlparams[0])
    except checkmod.ShippingAddress.DoesNotExist:
        return HttpResponseRedirect('/checkout/shipping/')

    # process the form
    form = PurchaseForm(request, cart_total = cart_total)
    if form.is_valid():
        sale_id = str(form.commit(usercart, cart_subtotal, cart_tax, cart_shipping, cart_total, ship_address))
        return HttpResponseRedirect('/checkout/receipt/' + sale_id)

    # render the template


    context = {
        'form' : form,
        'usercart' : usercart,
        'cart_subtotal' : cart_subtotal,
        'cart_tax' : cart_tax,
        'cart_shipping' : cart_shipping,
        'cart_total' : cart_total,
        'ship_address' : ship_address
    }
    return dmp_render(request, 'checkout.html', context)



class PurchaseForm(FormMixIn, forms.Form):
    form_id = 'checkout_form'
    form_submit = 'Pay Now'

    def init(self, cart_total):
        # add fields here
        self.fields['stripe_token'] = forms.CharField(label='Stipe-Token', required=False , widget=forms.HiddenInput())
        self.cart_total = cart_total
        self.charge = ''

    def clean(self):
        #Use Token to process charge on Stripe.
        stripe.api_key = settings.STRIPE_TEST_SECRET

        stripe_charge = stripe.Charge.create(
        amount = int(self.cart_total * Decimal('100')),
        currency = 'usd',
        source= self.cleaned_data.get('stripe_token'),
        description = 'Sale for ' + self.request.user.username
        )

        if stripe_charge.status != 'succeeded': #Raise Validation Error if charge does not succeed.
            raise forms.ValidationError('Card Error, please use another one.')
        else:
            self.charge = stripe_charge.id
        return self.cleaned_data

    def commit(self, usercart, cart_subtotal, cart_tax, cart_shipping, cart_total, ship_address):
        #retrieve charge created in clean()
        stripe_charge = stripe.Charge.retrieve(self.charge)





        #Record Sale in the Database
        user = self.request.user
        stripe_token = self.cleaned_data.get('stripe_token')
        sale = checkmod.Sale.record_sale(user, usercart, cart_subtotal, cart_tax, cart_shipping, cart_total, ship_address, stripe_charge)
        #empty cartTax
        for item in usercart:
            item.status = 'purchased'
            item.save()

        return sale.id
