from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from catalog import models as cmod
from account import models as amod
from django import forms
from formlib.form import FormMixIn
from django.contrib import messages

from .. import dmp_render, dmp_render_to_string



@view_function
@login_required(login_url='/account/login/')
def process_request(request):
    pid = request.urlparams[0]
    try:
        product = cmod.Product.objects.get(id=pid)
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/index/')

    if product.available == False:
        return HttpResponseRedirect('/catalog/index/')

    #Add History Item#
    historyitem = amod.HistoryItem()
    historyitem.FOMOUser = request.user
    historyitem.product = product
    historyitem.save()

    form = PurchaseForm(request, product=product)


    if form.is_valid():
        form.commit(historyitem)
        messages.success(request, 'Item successfully added to cart.')

    template_name = 'detail.html'
    if request.method =='POST':
        template_name = 'detail-ajax.html'


    return dmp_render(request, template_name, {
        'product' : product,
        'form' : form
    })

class PurchaseForm(FormMixIn, forms.Form):
    '''Purchase Form'''
    form_submit = 'Add to Cart'
    field_classes = ''
    # form_action = '/catalog/detail/'
    def init(self, product):
        #Initialize form values
        self.product=product
        if hasattr(product, 'quantity'):
            self.fields['quantity'] = forms.IntegerField(label='Quantity')

    def clean(self):
        usercart = self.request.user.retrieveCart()
        if hasattr(self.product, 'quantity'):
            qty_request = self.cleaned_data.get('quantity')
            qty_available = self.product.quantity
            if qty_request <= 0:
                raise forms.ValidationError('Quantity must be greater than 0')
            elif qty_request > qty_available:
                qty_stock = str(qty_available)
                raise forms.ValidationError('Only ' + qty_stock + ' in stock')

        for item in usercart:
            if self.product == item.product: #Check if item is already in the cart

                #Raise Validation Error if UniqueProduct or Rental Product is already in the cart
                if isinstance(self.product, cmod.UniqueProduct) or isinstance(self.product, cmod.RentalProduct):
                    raise forms.ValidationError('Item already in cart')

                #Raise Validation if sum of quantities is greater than amount available.
                if isinstance(self.product, cmod.BulkProduct):
                    if item.quantity + qty_request > qty_available:
                        qty_cart = str(item.quantity)
                        qty_remaining = str(qty_available - item.quantity)
                        raise forms.ValidationError(qty_cart + ' already in cart; ' + qty_remaining + ' remaining to buy' )
                    else: #Else update the forms quantity to sum and remove old cart item
                        self.cleaned_data['quantity'] = item.quantity + qty_request
                        item.status= 'removed'
                        item.save()
        return self.cleaned_data



    def commit(self, historyitem):
        if isinstance(historyitem.product, cmod.BulkProduct):
            quantity = self.cleaned_data.get('quantity')
        else:
            quantity = 1

        cartitem = amod.CartItem()
        cartitem.FOMOUser = self.request.user
        cartitem.product = historyitem.product
        cartitem.quantity = quantity
        cartitem.ext_price = historyitem.product.price * cartitem.quantity
        cartitem.status = 'active'
        cartitem.save()

        #change status of historyitem
        historyitem.status = 'cartitem'
        historyitem.save()


@view_function
def modal(request):
    pid = request.urlparams[0]
    pictures = cmod.ProductPicture.objects.filter(product_id=request.urlparams[0])


    context = {
        'pictures' : pictures
    }
    return dmp_render(request, 'detailmodule.html', context)
