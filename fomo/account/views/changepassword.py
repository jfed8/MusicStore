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
@permission_required('account.change_self')
def process_request(request):


    form = ChangePasswordForm(request)
    if form.is_valid():
        form.commit(request)
        #redirect to the my account page
        return HttpResponseRedirect('/account/myaccount/')

    #If not authenticated
    return dmp_render(request, 'changeself.html', {
        'form': form,
    })


class ChangePasswordForm(FormMixIn, forms.Form):
    '''Change Password form'''

    def init(self):
        '''Initializes the form fields.'''
        self.fields['oldpassword'] = forms.CharField(label='Current Password', required=True, widget=forms.PasswordInput())
        self.fields['newpassword'] = forms.CharField(label='New Password',required=True, widget=forms.PasswordInput())
        self.fields['confirmpassword'] = forms.CharField(label='Confirm Password',required=True, widget=forms.PasswordInput())

    def clean_oldpassword(self):
        oldpassword=self.cleaned_data.get('oldpassword')
        '''Authenticates user with old password'''
        user= authenticate(username=self.request.user.username, password=oldpassword)
        if user is None:
            raise forms.ValidationError('Invalid current password.')
        return oldpassword

    def clean(self):
        '''Verifies that new password is confirmed'''
        if self.cleaned_data.get('newpassword') != self.cleaned_data.get('confirmpassword'):
            raise forms.ValidationError('New passwords do not match.')
        return self.cleaned_data

    def commit(self, request):
        newpassword = self.cleaned_data.get('newpassword')
        print('>>>>>>>>>>>>>>>', newpassword)
        user=amod.FOMOUser.objects.get(id=self.request.user.id)
        print('>>>>>>>>>>>>>>>', user.username)
        user.set_password(newpassword)
        user.save()
        '''Login user again'''

        self.user = authenticate(username=user.username, password=newpassword)
        login(self.request, self.user)
