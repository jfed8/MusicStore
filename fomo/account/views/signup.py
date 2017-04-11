from django_mako_plus import view_function
from formlib.form import FormMixIn
from django import forms
from .. import dmp_render, dmp_render_to_string
from account import models as amod
from django.contrib.auth.models import Permission, Group
from datetime import date, datetime
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

@view_function
def process_request(request):

    # process the form
    form = SignUpForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/')

    # render the template
    return dmp_render(request, 'signup.html', {
        'form': form,
    })


class SignUpForm(FormMixIn, forms.Form):
    GENDER_CHOICES = [
        ['M', 'Male'],
        ['F', 'Female'],
        ['other', 'Other'],
    ]

    CONTACT_CHOICES = [
        ['text', 'Text'],
        ['email', 'Email'],
        ['voice', 'Voice'],
    ]

    def init(self):
        # add fields here
        self.fields['username'] = forms.CharField(label='Username')
        self.fields['password1'] = forms.CharField(label='Password', widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
        self.fields['first_name'] = forms.CharField(label='First Name')
        self.fields['last_name'] = forms.CharField(label='Last Name')
        self.fields['gender'] = forms.ChoiceField(label='Gender', choices=SignUpForm.GENDER_CHOICES)
        self.fields['birthday'] = forms.DateField(label='Birthday')
        self.fields['email'] = forms.EmailField(label='Email')
        self.fields['phone'] = forms.CharField(label='Phone')
        self.fields['pref_contact'] = forms.ChoiceField(label='Method of Contact', choices=SignUpForm.CONTACT_CHOICES)
        self.fields['address'] = forms.CharField(label='Address')
        self.fields['city'] = forms.CharField(label='City')
        self.fields['state'] = forms.CharField(label='State')
        self.fields['zipcode'] = forms.CharField(label='Zipcode')

    def clean_username(self):
        un = self.cleaned_data.get('username')
        duplicate = amod.FOMOUser.objects.filter(username=un)

        if len(duplicate)>0:
            raise forms.ValidationError('Username not available')
        return un

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('The passwords do not match.')
        return self.cleaned_data

    def commit(self):
            user = amod.FOMOUser()
            user.username = self.cleaned_data.get('username')
            print('>>>>>>>>>', self.cleaned_data.get('username'), '<<<<<<<')
            user.set_password(self.cleaned_data.get('password1'))
            user.last_login = datetime.now()
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.email = self.cleaned_data.get('email')
            user.is_staff = False
            user.is_superuser = False
            user.is_active = True
            user.date_joined = datetime.now()
            user.address = self.cleaned_data.get('address')
            user.city = self.cleaned_data.get('city')
            user.state = self.cleaned_data.get('state')
            user.zipcode = self.cleaned_data.get('zipcode')
            user.phone = self.cleaned_data.get('phone')
            user.pref_contact = self.cleaned_data.get('pref_contact')
            user.birthday = self.cleaned_data.get('birthday')
            user.gender = self.cleaned_data.get('gender')
            user.save()

            #Add user to Customer Group
            group = Group.objects.get(name='Customers')
            group.user_set.add(user)

            login(self.request, user)
