from django import forms

from .models import Book

class BookForm(forms.Form):
    title = forms.CharField(label="Название", required=True, widget=forms.TextInput(attrs={'class': 'form-input'}) )
    author = forms.CharField(label="Автор", required=True, widget=forms.Textarea(attrs={'cols': 50, 'rows': 2}))
    price = forms.IntegerField()


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields ='__all__'
        