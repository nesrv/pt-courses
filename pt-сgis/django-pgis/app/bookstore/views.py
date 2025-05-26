from django.shortcuts import render, HttpResponse, redirect

from time import asctime, strftime

from string import ascii_lowercase
from random import sample

from django.http import HttpResponse, JsonResponse
from os import getcwd,  listdir,  remove

from django.template.response import TemplateResponse

from .forms import AuthorForm

# Create your views here.


# def index(request):
#     return HttpResponse("<h1> Bookstore <h1>")

def index(request):
    return render(request, "index.html")

def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "index.html", context=data)

def get_book(request, book_name):
    return HttpResponse(f"<h1> {book_name} <h1>")


def get_year(request, year_id):
    return HttpResponse(f"<h1> {year_id} <h1>")


def current_time(request):
    return HttpResponse(f' {asctime().split()[3:]} ')


def workdir(request):
    return HttpResponse(f' {getcwd()} ')


def filelist(request):
    return HttpResponse(f' {listdir()} ')



def calculator(request, val_1 , val_2):
    return HttpResponse(f' {val_1}  + {val_2} = {val_1 + val_2}')

def f404(request, info):
    return HttpResponse(f'Непонятный адрес {info}')

def smart_calc(request, string):
    try:
        print(string)
        res = eval(string)
        return HttpResponse(f'<h1> Выражение {string} = {res} </h1>')
    except:
         return HttpResponse(f'Непонятный адрес {string}')
        #   return redirect('f404')


def json_response(request):
    return JsonResponse({"name": "Tom", "age": 38})

def get_requests(request):
    requests = request.__dict__
    print(request)
    return HttpResponse(f' {requests} ')


from .models import   Author

def get_authors(request):
    # authors = Author.objects.all()
    # authors = authors.filter(first_name__startswith='А')
    authors = Author.objects.raw('SELECT * FROM bookstore_author')
    return HttpResponse('123')


# def add_author(request):
#     form = AuthorForm()
#     return render(request, 'add_author.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create(**form.cleaned_data)
            # last_name = form.cleaned_data['last_name']
            # first_name = form.cleaned_data['first_name']
            # middle_name = form.cleaned_data['middle_name']
            # author = Author(last_name=last_name, first_name=first_name, middle_name=middle_name)
            # author.save()
            return redirect('get_authors')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})