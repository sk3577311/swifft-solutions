from dataclasses import fields
from pyexpat import model
from django import forms
from swifft.models import contactus


class contactus_form(forms.Form):
    class Meta:
        model = contactus
        fields = '__all__'
