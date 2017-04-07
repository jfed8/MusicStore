from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from catalog import models as cmod
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@permission_required('account.manager_menu')
def process_request(request):
    # Query all products
    '''
    .all()
    .filter(name='trumpet')
    .exclude()
    (list of Products)
    []
    [ Product ]

    try:
        .get(id=1233234)
    except cmod.Product.DoesNotExist:
        return HttpResponse(status_code=404)
        return HttpResponse('Not found buddy.')
        return HttpResponseRedirect('/manager/products')
        #what now?
        '''

    products = cmod.Product.objects.order_by('name').all()

    context = {
        'products': products
    }

    return dmp_render(request, 'products.html', context)


@view_function
def get_quantity(request):
    '''Function to get current quantity of product id in urlparams[0]'''
    try:
        product = cmod.BulkProduct.objects.get(id=request.urlparams[0])

    except cmod.BulkProduct.DoesNotExist:
        return HttpResponseRedirect('/manager/products/')

    return HttpResponse(product.quantity)
