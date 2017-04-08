from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from catalog import models as cmod
from account import models as amod
from django import forms
from formlib.form import FormMixIn

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
        quantity = getattr(product, 'quantity', None)

        if quantity is not None:
            self.fields['quantity'] = forms.IntegerField(label='Quantity')

    def clean_quantity(self):
        '''Check Quantity'''
        qty_request = self.cleaned_data.get('quantity')
        qty_available = self.product.quantity
        user = self.request.user
        if qty_request <= 0:
            raise forms.ValidationError('Quantity must be greater that 0')
        elif qty_request > qty_available:
            raise forms.ValidationError('Not enough in stock')

        return qty_request

    def clean(self):
        usercart = self.request.user.retrieveCart()

        for item in usercart:
            if self.product == item.product: #Check if item is already in the cart

                #Raise Validation Error if UniqueProduct or Rental Product is already in the cart
                if isinstance(self.product, cmod.UniqueProduct) or isinstance(self.product, cmod.RentalProduct):
                    raise forms.ValidationError('Item already in cart')

                #Raise Validation if sum of quantities is greater than amount available.
                if isinstance(self.product, cmod.BulkProduct):
                    if item.quantity + self.cleaned_data.get('quantity') > self.product.quantity:
                        raise forms.ValidationError('Not enough in stock')
                    else: #Else update the forms quantity to sum and remove old cart item
                        self.cleaned_data['quantity'] = item.quantity + self.cleaned_data.get('quantity')
                        item.status= 'removed'
                        item.save()




        self.cleaned_data



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
