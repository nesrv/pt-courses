from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
#
from .models import Book
from .forms import BookForm, AddBookForm


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
  
    form = AddBookForm()
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books, 'form' :form })    


def index(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
       
    books = Book.objects.all()
    header =  {"header": "Лабиринт"}
    form = BookForm()
    
    data = {
        'header': header,
        'books': books,
        'form': form      
    }

    return TemplateResponse(request,  "index.html", context = data)

# book2 = Book(title='Мастер и Маргарита', author='Булгаков', price=15)
# book3 = Book(title='Евгений Онегин', author='Пушкин', price=20)
# book4 = Book(title='Война и мир', author='Толстой', price=25)

# book2.save()
# book3.save()
# book4.save()

def about(requests):
    return HttpResponse ("<h2> Лучший магазин <h2>")


