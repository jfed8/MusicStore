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
from django.core.mail import send_mail

from .. import dmp_render, dmp_render_to_string

@view_function
@login_required(login_url='/account/login/')
def process_request(request):
    try:
        sale = checkmod.Sale.objects.get(id=request.urlparams[0])
    except checkmod.Sale.DoesNotExist:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>, Sale not found')
        return HttpResponseRedirect('/')

    try:
        shippingaddress = checkmod.ShippingAddress.objects.get(id= sale.ship_address.id)
    except checkmod.ShippingAddress.DoesNotExist:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>, ShippingAddress not found')
        return HttpResponseRedirect('/')

    try:
        payment = checkmod.Payment.objects.get(sale_id= sale.id)
    except checkmod.Payment.DoesNotExist:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>, Payment not found')
        return HttpResponseRedirect('/')

    saleitems = checkmod.SaleItem.objects.filter(sale_id= sale.id)

    context = {

        'sale' : sale,
        'shippingaddress' : shippingaddress,
        'payment' : payment,
        'saleitems' : saleitems,
    }

    # #send email
    # from_name = 'FOMO Customer Support'
    # from_email = settings.DEFAULT_FROM_EMAIL
    # subject = "Order Receipt"
    # message = ''
    # to_email = 'klynt.yardley@gmail.com'
    # html_message = dmp_render_to_string(request, 'receipt-ajax.html', context)
    # print(html_message)
    # if from_email != '':
    #     send_mail(
    #             subject,
    #             message,
    #             from_email,
    #             [to_email],
    #             fail_silently=False,
    #             html_message=html_message,
    #         )

    return dmp_render(request, 'receipt.html', context)
