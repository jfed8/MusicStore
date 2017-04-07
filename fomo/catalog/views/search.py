from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from catalog import models as cmod

@view_function
def process_request(request):


    user_input = request.GET.get('product_name')
    if user_input is None:
        return HttpResponseRedirect('/catalog/')

    products = cmod.Product.objects.filter(name__icontains=user_input)

    context = {
        'products' : products
    }
    return dmp_render(request, 'search.html', context)
