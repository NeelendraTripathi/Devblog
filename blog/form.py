# blog/forms.py
from django import forms

# This class defines our contact form blueprint.
class ContactForm(forms.Form):
    # A CharField for the user's name. label="" sets the display name.
    # widget=... allows us to set HTML attributes, like a CSS class and a placeholder.
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Name'})
    )

    # An EmailField that automatically validates the email format.
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your Email'})
    )

    # A CharField with a Textarea widget for a larger message box.
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Your Message'}))
