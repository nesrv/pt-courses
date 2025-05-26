from django import forms
from .models import Author

# Использование форм не связанных с моделями

class AuthorForm(forms.Form):
    last_name = forms.CharField(label='Last Name', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    middle_name = forms.CharField(label='Middle Name', max_length=100, required=False)
    
    

