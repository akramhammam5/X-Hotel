from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'example@domain.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Explain your queries'}))