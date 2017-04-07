from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from catalog import models as cmod
from decimal import Decimal
from django.contrib.auth.decorators import login_required, permission_required
from formlib.form import FormMixIn
from django import forms


@view_function
@permission_required('catalog.add_product')
def process_request(request):

    # process the form
    form = CreateProductForm(request)
    if form.is_valid():
        d = form.commit()
        return HttpResponseRedirect('/manager/products/')

    # render the template
    return dmp_render(request, 'createproduct.html', {
        'form': form,
    })


class CreateProductForm(FormMixIn, forms.Form):
    PRODUCT_CHOICES = [
        ['BulkProduct', 'Bulk Product'],
        ['UniqueProduct', 'Unique Product'],
        ['RentalProduct', "Rental Product"],

    ]
    def init(self):
        '''Initialize the form (called at end of __init__)'''
        #Product Fields
        self.fields['product_type'] = forms.ChoiceField(label='Product Type', choices= CreateProductForm.PRODUCT_CHOICES)
        self.fields['name'] = forms.CharField(label="Product Name", max_length=100)
        self.fields['category'] = forms.ModelChoiceField(label='Category',
            queryset=cmod.Category.objects.order_by('name').all())
        self.fields['price'] = forms.DecimalField(label='Price')
        self.fields['graphic'] = forms.CharField(label='Graphic')
        #BulkProduct Fields:
        self.fields['barcode'] = forms.CharField(label='Barcode', required=False)
        self.fields['quantity'] = forms.IntegerField(label='Quantity', required=False)
        self.fields['reorder_trigger'] = forms.IntegerField(label='Reorder Trigger', required=False)
        self.fields['reorder_quantity'] = forms.IntegerField(label='Reorder Quantity', required=False)
        #UniqueProduct Fields:
        self.fields['serial_number'] = forms.CharField(label='Serial Number', required=False)
        self.fields['condition'] = forms.CharField(label='Condition', required=False)
        #RentalProduct Fields
        self.fields['is_rented'] = forms.BooleanField(label='Is rented', required=False)
        self.fields['due_date'] = forms.DateField(label='Due Date', required=False)


    def commit(self):
        '''Process the form action'''
        if (self.cleaned_data['product_type'] == 'BulkProduct'):
            bulkproduct = cmod.BulkProduct()
            bulkproduct.name = self.cleaned_data['name']
            cat1 = cmod.Category.objects.get(name=self.cleaned_data['category'])
            bulkproduct.category = cat1
            bulkproduct.price = Decimal(self.cleaned_data['price'])
            bulkproduct.graphic = self.cleaned_data['graphic']
            bulkproduct.barcode = self.cleaned_data['barcode']
            bulkproduct.quantity = self.cleaned_data['quantity']
            bulkproduct.reorder_trigger = self.cleaned_data['reorder_trigger']
            bulkproduct.reorder_quantity = self.cleaned_data['reorder_quantity']
            bulkproduct.save()

        if (self.cleaned_data['product_type'] == 'UniqueProduct'):
            uniqueproduct = cmod.UniqueProduct()
            uniqueproduct.name = self.cleaned_data['name']
            cat1 = cmod.Category.objects.get(name=self.cleaned_data['category'])
            uniqueproduct.category = cat1
            uniqueproduct.price = Decimal(self.cleaned_data['price'])
            uniqueproduct.graphic = self.cleaned_data['graphic']
            uniqueproduct.serial_number = self.cleaned_data['serial_number']
            uniqueproduct.condition = self.cleaned_data['condition']
            uniqueproduct.save()

        if (self.cleaned_data['product_type'] == 'RentalProduct'):
            rentalproduct = cmod.RentalProduct()
            rentalproduct.name = self.cleaned_data['name']
            cat1 = cmod.Category.objects.get(name=self.cleaned_data['category'])
            rentalproduct.category = cat1
            rentalproduct.price = Decimal(self.cleaned_data['price'])
            rentalproduct.graphic = self.cleaned_data['graphic']
            rentalproduct.serial_number = self.cleaned_data['serial_number']
            rentalproduct.is_rented = self.cleaned_data['is_rented']
            rentalproduct.condition = self.cleaned_data['condition']
            rentalproduct.due_date = self.cleaned_data['due_date']
            rentalproduct.save()
