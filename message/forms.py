from django.forms import ModelForm, TextInput, Textarea
from message.models import ContactMessage,subscrib 
from django import forms
from django.core.exceptions import ValidationError
class ContactForm(ModelForm):

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name'   : forms.TextInput(attrs={'class': 'input','placeholder':'Name & Surname'}),
            'subject' : forms.TextInput(attrs={'class': 'input','placeholder':'Subject'}),
            'email'   : forms.EmailInput(attrs={'class': 'input','placeholder':'Email Address'}),
            'message' : forms.Textarea(attrs={'class': 'input','placeholder':'Your Message','rows':'5'}),
        }
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100,required=True)
#     subject = forms.CharField(max_length=100,required=True)
#     email = forms.EmailField(required=True)
#     message = forms.CharField(required=True)
    
    
    # cc_myself = forms.BooleanField(required=False)
class subscribForm(forms.Form):
    email = forms.EmailField()
    

    