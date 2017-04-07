from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django_mako_plus import view_function
from django.contrib.auth import authenticate, login
from django import forms
from formlib.form import FormMixIn

from .. import dmp_render, dmp_render_to_string

@view_function
def process_request(request):
    #Process form
    form = LoginForm(request)
    if form.is_valid():
        form.commit(request)
        #redirect to the my account page
        return HttpResponseRedirect('/account/myaccount')

    #If not authenticated
    return dmp_render(request, 'login.html', {
        'form': form,
    })

@view_function
def modal(request):
    #Process form
    form = ModalLoginForm(request)
    if form.is_valid():
        form.commit(request)
        #redirect to the my account page
        return HttpResponse('''
            <script>
                window.location.href = '/homepage/index/';
            </script>
        ''')

    #If not authenticated
    return dmp_render(request, 'loginmodal.html', {
        'form': form,
    })




class LoginForm(FormMixIn, forms.Form):
    '''The Login form'''

    def init(self):
        '''Initializes the form fields.'''
        #fields
        self.fields['username'] = forms.CharField(required=True)
        self.fields['password'] = forms.CharField(required=True, widget=forms.PasswordInput())

    def clean(self):
        '''Authenticates the username and password'''
        user= authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError('Invalid username or password.')

        return self.cleaned_data

    def commit(self, request):
        user= authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        login(request, user)

class ModalLoginForm(LoginForm):
    form_action = '/account/login.modal/'
