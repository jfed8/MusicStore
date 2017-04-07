from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from account import models as amod
from django import forms
from formlib.form import FormMixIn
from .. import dmp_render, dmp_render_to_string
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, Group

@view_function
@permission_required('account.change_fomouser')
def process_request(request):
    try:
        user = amod.FOMOUser.objects.get(id=request.urlparams[0])
    except amod.FOMOUser.DoesNotExist:
        return HttpResponseRedirect('/account/myaccount/')


    form = EditUserForm(request, user=user, initial={
        'username' : user.username,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'gender' : user.gender,
        'birthday' : user.birthday,
        'email' : user.email,
        'phone' : user.phone,
        'pref_contact' : user.pref_contact,
        'address' : user.address,
        'city' : user.city,
        'state' : user.state,
        'zipcode' : user.zipcode,
        'groups': user.groups.all(),
        'permissions': user.user_permissions.all(),
        'is_staff' : user.is_staff,
        'is_active' : user.is_active,
        'is_superuser' : user.is_superuser,
    })
    if form.is_valid():
        form.commit(user)
        #redirect to the my account page
        return HttpResponseRedirect('/manager/users')

    #If not authenticated
    return dmp_render(request, 'manageuser.html', {
        'form': form,
    })


class EditUserForm(FormMixIn, forms.Form):
    '''Edit Self form'''
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

    def init(self, user):
        '''Initializes the form fields.'''
        self.fields['username'] = forms.CharField(label='Username')
        self.fields['first_name'] = forms.CharField(label='First Name')
        self.fields['last_name'] = forms.CharField(label='Last Name')
        self.fields['gender'] = forms.ChoiceField(label='Gender', choices=EditUserForm.GENDER_CHOICES)
        self.fields['birthday'] = forms.DateField(label='Birthday')
        self.fields['email'] = forms.EmailField(label='Email')
        self.fields['phone'] = forms.CharField(label='Phone')
        self.fields['pref_contact'] = forms.ChoiceField(label='Method of Contact', choices=EditUserForm.CONTACT_CHOICES)
        self.fields['address'] = forms.CharField(label='Address')
        self.fields['city'] = forms.CharField(label='City')
        self.fields['state'] = forms.CharField(label='State')
        self.fields['zipcode'] = forms.CharField(label='Zipcode')
        self.fields['permissions'] = forms.ModelMultipleChoiceField(label='Permissions',
            queryset=Permission.objects.order_by('name').all(), required=False)
        self.fields['groups'] = forms.ModelMultipleChoiceField(label='Group',
            queryset=Group.objects.order_by('name').all())
        self.fields['is_staff'] = forms.BooleanField(label='Is Staff', required=False)
        self.fields['is_active'] = forms.BooleanField(label='Is Active', required=False)
        self.fields['is_superuser'] = forms.BooleanField(label='Is Superuser', required=False)

    def clean_username(self):
        cleanName = self.cleaned_data.get('username')
        print('>>>>>cleanName: ', cleanName)
        print('>>>>>>>>>>>>>>>>>>>>>>>', self.request.urlparams[0])
        users = amod.FOMOUser.objects.filter(username=cleanName).exclude(id=self.request.urlparams[0])
        print('>>>>>>>>',len(users))
        if len(users) > 0:
            raise forms.ValidationError("That username already exists")
        return cleanName


    def commit(self, user):
        p = self.cleaned_data.get('permissions')
        g = self.cleaned_data.get('groups')
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.gender = self.cleaned_data.get('gender')
        user.birthday = self.cleaned_data.get('birthday')
        user.email = self.cleaned_data.get('email')
        user.phone = self.cleaned_data.get('phone')
        user.pref_contact = self.cleaned_data.get('pref_contact')
        user.address = self.cleaned_data.get('address')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.zipcode = self.cleaned_data.get('zipcode')
        user.is_staff = self.cleaned_data.get('is_staff')
        user.is_staff = self.cleaned_data.get('is_staff')
        user.is_superuser = self.cleaned_data.get('is_superuser')
        user.save()

        #Remove user from current perms and groups
        user.groups.clear()
        user.user_permissions.clear()

        ###Assign new perms and groups from form
        for SinglePermission in p:
            user.user_permissions.add(SinglePermission)
            print('>>>>>', SinglePermission, '<<<<<')
        for SingleGroup in g:
            user.groups.add(SingleGroup)
            print('>>>>>', SingleGroup, '<<<<<')
        user.save()


##################################################################################
''' DELETING A User'''

@view_function
@permission_required('account.delete_fomouser')
def delete(request):
    try:
        user = amod.FOMOUser.objects.get(id=request.urlparams[0])
    except cmdo.Product.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')

    user.delete()
    return HttpResponseRedirect('/manager/users/')
