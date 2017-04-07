from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from account import models as amod
from django.contrib.auth.decorators import login_required, permission_required


@view_function
@permission_required('account.manager_menu')
def process_request(request):
    # Query all users


    users = amod.FOMOUser.objects.order_by('first_name').all()

    context = {
        'users': users
    }

    return dmp_render(request, 'users.html', context)
