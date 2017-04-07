from django.conf import settings
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from catalog import models as cmod

from .. import dmp_render, dmp_render_to_string



@view_function
@login_required(login_url='/account/login/')
def process_request(request):

    categories = cmod.Category.objects.order_by('name').all()



    products = cmod.Product.objects.order_by('name').filter(available = True)

    context = {
        'products': products,
        'categories' : categories
    }

    return dmp_render(request, 'index.html', context)


@view_function
def filter(request):

    categories = cmod.Category.objects.order_by('name').all()



    products = cmod.Product.objects.order_by('name').filter(category_id=request.urlparams[0])

    context = {
        'products': products,
        'categories' : categories
    }

    return dmp_render(request, 'index.html', context)
