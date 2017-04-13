from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from checkout import models as checkmod
from .. import dmp_render, dmp_render_to_string

@view_function
def process_request(request):

    orders = request.user.retrieveOrders()

    context = {
        'orders' : orders
    }
    return dmp_render(request, 'orderhistory.html', context)
