from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
       model=Contactus
       fields = ('name', 'email', 'phone', 'header', 'message')