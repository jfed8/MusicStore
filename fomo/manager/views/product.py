from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from catalog import models as cmod
from django.contrib.auth.decorators import login_required, permission_required

from formlib.form import FormMixIn
from django import forms

@view_function
@permission_required('catalog.change_product')
def process_request(request):

    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])

    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/manager/products/')

    # process the form
    form = ProductEditForm(request, product=product, initial= {
        'name': product.name,
        'category': product.category,
        'price': product.price,
        'graphic' : product.graphic,
        #BulkProduct
        'barcode': getattr(product, 'barcode', 0),
        'quantity': getattr(product, 'quantity', 0),
        'reorder_trigger': getattr(product, 'reorder_trigger', 0),
        'reorder_quantity': getattr(product, 'reorder_quantity', 0),
        #UniqueProduct
        'serial_number': getattr(product, 'serial_number', 0),
        'barcode': getattr(product, 'barcode', 0),
        'condition': getattr(product, 'condition', 0),
        #RentalProduct
        'is_rented': getattr(product, 'is_rented', 0),
        'due_date': getattr(product, 'due_date', 0),

    })
    if form.is_valid():
        form.commit(product)
        return HttpResponseRedirect('/manager/products/')

    context = {
        'product': product,
        'form': form,
    }

    return dmp_render(request, 'product.html', context)



class ProductEditForm(FormMixIn, forms.Form):
    def init(self, product):
        '''Initialize the form (called at end of __init__)'''
        # add fields here
        #Product Fields:
        self.fields['name'] = forms.CharField(label="Product Name", max_length=100)
        self.fields['category'] = forms.ModelChoiceField(label='Category',
            queryset=cmod.Category.objects.order_by('name').all())
        self.fields['price'] = forms.DecimalField(label='Price')
        self.fields['graphic'] = forms.CharField(label='Graphic')
        #BulkProduct Fields:
        if hasattr(product, 'barcode'):
            self.fields['barcode'] = forms.CharField(label='Barcode')
        if hasattr(product, 'quantity'):
            self.fields['quantity'] = forms.IntegerField(label='Quantity')
        if hasattr(product, 'reorder_trigger'):
            self.fields['reorder_trigger'] = forms.IntegerField(label='Reorder Trigger')
        if hasattr(product, 'reorder_quantity'):
            self.fields['reorder_quantity'] = forms.IntegerField(label='Reorder Quantity')

        #UniqueProduct Fields:
        if hasattr(product, 'serial_number'):
            self.fields['serial_number'] = forms.CharField(label='Serial Number')
        if hasattr(product, 'condition'):
            self.fields['condition'] = forms.CharField(label='Condition')

        #RentalProduct Fields
        if hasattr(product, 'is_rented'):
            self.fields['is_rented'] = forms.BooleanField(label='Is rented', required=False)
        if hasattr(product, 'due_date'):
            self.fields['due_date'] = forms.DateField(label='Due Date', required=False)


    def commit(self, product):
        '''Process the form action'''
        product.name = self.cleaned_data.get('name')
        product.category = self.cleaned_data.get('category')
        product.price = self.cleaned_data.get('price')
        product.graphic = self.cleaned_data.get('graphic')
        #BulkProduct
        if hasattr(product, 'barcode'):
            product.barcode = self.cleaned_data.get('barcode')
        if hasattr(product, 'quantity'):
            product.quantity = self.cleaned_data.get('quantity')
        if hasattr(product, 'reorder_trigger'):
            product.reorder_trigger = self.cleaned_data.get('reorder_trigger')
        if hasattr(product, 'reorder_quantity'):
            product.reorder_quantity = self.cleaned_data.get('reorder_quantity')
        #UniqueProduct
        if hasattr(product, 'serial_number'):
            product.serial_number = self.cleaned_data.get('serial_number')
        if hasattr(product, 'condition'):
            product.condition = self.cleaned_data.get('condition')
        #RentalProduct
        if hasattr(product, 'is_rented'):
            product.is_rented = self.cleaned_data.get('is_rented')
        if hasattr(product, 'due_date'):
            product.due_date = self.cleaned_data.get('due_date')
        #############
        product.save()



##################################################################################
''' DELETING A PRODUCT'''

@view_function
@permission_required('catalog.delete_product')
def delete(request):
    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmdo.Product.DoesNotExist:
        return HttpResponseRedirect('/manager/products/')

    product.delete()
    return HttpResponseRedirect('/manager/products/')
