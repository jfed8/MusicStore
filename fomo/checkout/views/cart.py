from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from account import models as amod
from catalog import models as cmod
from django.http import HttpResponseRedirect, HttpResponse
from .. import dmp_render, dmp_render_to_string

@view_function
@login_required(login_url='/account/login/')
def process_request(request):



    context = {

    }
    return dmp_render(request, 'cart.html', context)



@view_function
@login_required(login_url='/account/login/')
def emptyCart(request):
    request.user.emptyCart()
    return HttpResponseRedirect('/checkout/cart/')


@view_function
@login_required(login_url='/account/login/')
def removeItem(request):
    print('>>>>>>>>>>>>>>>>>>>>>>AM I FOUND?')
    try:
        cartitem = amod.CartItem.objects.get(id=request.urlparams[0])
    except amod.CartItem.DoesNotExist:
        return HttpResponseRedirect('/checkout/cart/')

    cartitem.removeItem()
    print('>>>>>>>>>>>>>>>>>>>>>>', cartitem.status)
    return HttpResponseRedirect('/checkout/cart/')
