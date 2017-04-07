from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseNotFound
from django_mako_plus import view_function
from django.contrib.auth import authenticate, login
from django import forms
from formlib.form import FormMixIn
from .. import dmp_render, dmp_render_to_string
import json
from catalog import models as cmod

@view_function
def process_request(request):
    product_name = request.GET.get('product_name')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category_name = request.GET.get('category_name')

    #Query Database for products that match
    products = cmod.Product.objects.all()
    if product_name:
        products = products.filter(name__icontains = product_name)
    if min_price:
        try:
            float(min_price)
        except ValueError:
            return HttpResponseNotFound('Minimum Price Invalid')
        products = products.filter(price__gte=min_price)
    if max_price:
        try:
            float(max_price)
        except ValueError:
            return HttpResponseNotFound('Maximum Price Invalid')
        products = products.filter(price__lte=max_price)
    if category_name:
        products = products.filter(category__name__icontains=category_name)



    json_products = []
    for p in products:
        if isinstance(p, cmod.BulkProduct):
            ret = {
            'Product Type' : 'Bulk Product',
            'name' : p.name,
            'category' : p.category.name,
            'price' : p.price,
            'barcode' : p.barcode,
            'quantity' : p.quantity,
            }

        if isinstance(p, cmod.UniqueProduct):
            ret = {
            'Product Type' : 'Unique Product',
            'name' : p.name,
            'category' : p.category.name,
            'price' : p.price,
            'serial_number' : p.serial_number,
            'condition' : p.condition,
            }

        if isinstance(p, cmod.RentalProduct):
            ret = {
            'Product Type' : 'Rental Product',
            'name' : p.name,
            'category' : p.category.name,
            'price' : p.price,
            'serial_number' : p.serial_number,
            'condition' : p.condition,
            'is_rented' : p.is_rented
            }

        json_products.append(ret)




    return JsonResponse(json_products, safe=False)
