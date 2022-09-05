from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(label='Your Name', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
  email_address = forms.EmailField(label='Your Email', max_length=64, widget=forms.EmailInput(attrs={'class': 'form-control'}))
  subject = forms.CharField(label='Subject', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
  message = forms.CharField(label='Your Message', max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control'}))
  