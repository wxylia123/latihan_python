from django import forms
from django.core import validators

class FormName (forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label ='input your email again :')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data.get('email')
        vemail = all_clean_data.get('verify_email')
 
        if email != vemail:
            raise forms.ValidationError("Make sure emails match!")

