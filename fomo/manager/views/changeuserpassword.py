from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from account import models as amod
from django import forms
from formlib.form import FormMixIn
from django.contrib.auth import authenticate, login
from .. import dmp_render, dmp_render_to_string
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@permission_required('account.change_fomouser')
def process_request(request):


    form = ChangePasswordForm(request)
    if form.is_valid():
        form.commit(request)
        #redirect to the my account page
        return HttpResponseRedirect('/manager/users/')

    #If not authenticated
    return dmp_render(request, 'changeuserpassword.html', {
        'form': form,
    })


class ChangePasswordForm(FormMixIn, forms.Form):
    '''Change Password form'''

    def init(self):
        '''Initializes the form fields.'''
        self.fields['newpassword'] = forms.CharField(label='New Password',required=True, widget=forms.PasswordInput())
        self.fields['confirmpassword'] = forms.CharField(label='Confirm Password',required=True, widget=forms.PasswordInput())

    def clean(self):
        '''Verifies that new password is confirmed'''
        if self.cleaned_data.get('newpassword') != self.cleaned_data.get('confirmpassword'):
            raise forms.ValidationError('New passwords do not match.')
        return self.cleaned_data

    def commit(self, request):
        newpassword = self.cleaned_data.get('newpassword')
        user=amod.FOMOUser.objects.get(username=self.request.urlparams[0])
        user.set_password(newpassword)
        user.save()
