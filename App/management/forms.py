# Django Import:
from django import forms

# Application Import:
from .models import (
    Device,
)

class AddDeviceForm(forms.ModelForm):
    
    class Meta:
        model = Device
        fields = ('name', 'hostname', 'credential')


class TestForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='mail')
    options = forms.ChoiceField(choices=[('one', 'One'), ('two', 'Two')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)