from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django_mako_plus import view_function
from django.contrib.auth import authenticate, login
from django import forms
from formlib.form import FormMixIn
from account import models as amod
from datetime import date, datetime

from .. import dmp_render, dmp_render_to_string
from ldap3 import Server, Connection, ALL, BASE, LEVEL, SUBTREE

@view_function
def process_request(request):
    #Process form
    form = LoginForm(request)
    if form.is_valid():
        form.commit(request)
        #redirect to the my account page
        return HttpResponseRedirect('/catalog/index/')

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
                window.location.href = '/catalog/index/';
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
            # define the server
            server = Server('thefomomusic.com', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema
            # define the connection
            conn = Connection(server,(self.cleaned_data['username']+'@thefomomusic.local'), self.cleaned_data['password'])
            if not conn.bind():
                raise forms.ValidationError('Invalid username or password.')
            if conn.bind():
                
                conn.search(search_base = 'cn=Users,dc=thefomomusic,dc=local',
                         search_filter = '(&(objectClass=Person)(userPrincipalName='+conn.user+'))',
                         search_scope = SUBTREE,
                         attributes = ['givenName', 'sn', 'userPrincipalName'])
                
                #raise forms.ValidationError('Welcome AD User - ' + str(conn.response[0]['attributes']['sn']))
                ad_user = amod.FOMOUser()
                ad_user.first_name = conn.response[0]['attributes']['givenName']
                ad_user.last_name = conn.response[0]['attributes']['sn']
                ad_user.email = 'test@mailinator.com'
                ad_user.username = self.cleaned_data['username']
                ad_user.set_password(conn.password)
                ad_user.is_staff = True
                ad_user.is_active = True
                ad_user.last_login = datetime.now()
                ad_user.is_superuser = True
                ad_user.save()

        return self.cleaned_data

    def commit(self, request):
        user= authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        login(request, user)

class ModalLoginForm(LoginForm):
    form_action = '/account/login.modal/'
