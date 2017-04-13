from django.conf import settings
from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib.form import FormMixIn
from django.core.mail import send_mail

from .. import dmp_render, dmp_render_to_string

@view_function
def process_request(request):

    form = ContactForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/homepage/contact.success/')





    return dmp_render(request, 'contact.html', {
        'form':form,
    })

@view_function
def success(request):

    return dmp_render(request, 'success.html', {
    })

class ContactForm(FormMixIn, forms.Form):

    SUBJECT_CHOICES = [
        ['payment', 'Payment Issue'],
        ['complaint', 'Complaint Issue'],
        ['login', "Login Issues"],
        ['other', "Other Issue"],
    ]

    def init(self):
        self.fields['name'] = forms.CharField(label='Full Name', max_length=100)
        self.fields['email'] = forms.EmailField(label='Email', max_length=100)
        # choices = ContactForm.SUBJECT_CHOICES[:]
        # if self.request.user.is_superuser:
        #     choices.append(['Reports', 'Reports Issue'])
        self.fields['subject'] = forms.ChoiceField(label='Subject', choices=ContactForm.SUBJECT_CHOICES)
        self.fields['message'] = forms.CharField(label='Message', max_length=1000, widget=forms.Textarea())

    def clean_name(self):  #Called automatically by form.siz_valid()
        name = self.cleaned_data.get('name')
        parts = name.strip().split()  #strips whitespace on either end #splits it by whitespace as default
        if len(parts) <=1:
            raise forms.ValidationError('Please enter both first and last name')
        return name

    def commit(self):
        #act on the form here
        #send email
        from_name = self.cleaned_data.get('name')
        from_email = self.cleaned_data.get('email')
        subject = self.cleaned_data.get('subject')
        message = self.cleaned_data.get('message')
        to_email = 'klynty@thefomomusic.com'
        if from_email != '':
            send_mail(
                    subject,
                    message,
                    from_email,
                    [to_email],
                    fail_silently=False,
                )
