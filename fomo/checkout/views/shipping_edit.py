from django.conf import settings
from django_mako_plus import view_function
from formlib.form import FormMixIn
from django import forms
from .. import dmp_render, dmp_render_to_string
from account import models as amod
from checkout import models as checkmod
from django.contrib.auth.models import Permission, Group
from datetime import date, datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@login_required(login_url='/account/login/')
def process_request(request):
    try:
        shippingaddress = checkmod.ShippingAddress.objects.get(id=request.urlparams[0])
    except checkmod.ShippingAddress.DoesNotExist:
        return HttpResponseRedirect('/')

    # process the form
    form = EditShippingForm(request, initial = {
        'fullname' :shippingaddress.fullname,
        'address' :shippingaddress.address,
        'city' :shippingaddress.city,
        'state' :shippingaddress.state,
        'zipcode' :shippingaddress.zipcode,
        'phone' : shippingaddress.phone,
    })
    if form.is_valid():
        form.commit(shippingaddress)
        return HttpResponseRedirect('/checkout/checkout/' + str(shippingaddress.id))

    # render the template
    return dmp_render(request, 'shipping_edit.html', {
        'form': form,
    })


class EditShippingForm(FormMixIn, forms.Form):

    def init(self):
        # add fields here
        self.fields['fullname'] = forms.CharField(label='Full Name', required=False)
        self.fields['address'] = forms.CharField(label='Address', required=False)
        self.fields['city'] = forms.CharField(label='City', required=False)
        self.fields['state'] = forms.CharField(label='State', required=False)
        self.fields['zipcode'] = forms.CharField(label='Zipcode', required=False)
        self.fields['phone'] = forms.CharField(label='Phone', required=False)



    def clean(self):
        return self.cleaned_data

    def commit(self, shippingaddress):
        shippingaddress.fullname = self.cleaned_data.get('fullname')
        shippingaddress.address = self.cleaned_data.get('address')
        shippingaddress.city = self.cleaned_data.get('city')
        shippingaddress.state = self.cleaned_data.get('state')
        shippingaddress.zipcode = self.cleaned_data.get('zipcode')
        shippingaddress.phone = self.cleaned_data.get('phone')
        shippingaddress.save()
