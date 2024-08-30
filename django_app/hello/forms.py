from django import forms

class HelloForm(forms.Form):
    check = forms.NullBooleanField(label='check')
    
