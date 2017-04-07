from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from account import models as amod
from django.contrib.auth.decorators import login_required, permission_required
from .. import dmp_render, dmp_render_to_string

@view_function
@login_required(login_url='/account/login/')
def process_request(request):

    current_user =request.user.id
    user = amod.FOMOUser.objects.get(id=current_user)

    context = {
        'user': user
    }
    return dmp_render(request, 'myaccount.html', context)
