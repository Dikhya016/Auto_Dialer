# contacts/forms.py
from django import forms
from .models import Phonebook, Contact


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class PhonebookForm(forms.ModelForm):
    class Meta:
        model = Phonebook
        fields = ['name']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'city', 'phone_number', 'phonebooks']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if user:
           self.fields['phonebooks'].queryset = Phonebook.objects.filter(user=user)
