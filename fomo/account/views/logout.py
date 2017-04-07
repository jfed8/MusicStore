from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required

from .. import dmp_render, dmp_render_to_string

@view_function
@login_required(login_url='/account/login/')
def process_request(request):
    #log the user in
    if request.user.is_authenticated:
        logout(request)

    # Redirect after logout
    return HttpResponseRedirect('/')
