from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(required=True, widget=forms.TextInput(
  attrs = {
    'class': "form-control",
    'placeholder': "Name",
    'autocomplete': 'off'
  }))

  email = forms.EmailField(required=True, widget=forms.TextInput(
  attrs = {
    'class': "form-control",
    'placeholder': "Email Address",
    'autocomplete': 'off'
  }))

  phone = forms.CharField(required=False, widget=forms.TextInput(
  attrs = {
    'class': "form-control",
    'placeholder': "Phone Number",
    'autocomplete': 'off'
  }))

  message = forms.CharField(required=False, widget=forms.Textarea(
  attrs = {
    'class': "form-control",
    'placeholder': "Message",
    'autocomplete': 'off'
  }))