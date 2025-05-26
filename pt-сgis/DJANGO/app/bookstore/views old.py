from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
#
# def index(request):
#     t = render_to_string('путь к шаблону index.html')
#     return HttpResponse(t)
#     # return render(request, "index.html")

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Клиент {self.name}'

def index(request):
    header =  {"header": "Лабиринт"}
    books = ['Муму', "Онегин", "Колобок"]
    langs = ["Python", "Java", "C#"]
    user = {"name": "Tom", "age": 23}
    address = ("Абрикосовая", 23, 45)
    person = Person("Айрат")
    data = {
        'header':header,
        'books':books,
        'langs':langs,
        'address':address,
        'person':person,
        'user':user
    }

    return TemplateResponse(request,  "index.html", context = data)


def about(requests):
    return HttpResponse ("<h2> Лучший магазин <h2>")


def login(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    people = ["Tom", "Bob", "Sam"]
    if int(age) < 18:
        return HttpResponseForbidden("Доступ запрешен. Мало лет") # 403
    if name in people:
        return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

    return HttpResponseNotFound("Пользователь не найден")


# 304 (Not Modified) # HttpResponseNotModified#
# 400 (Bad Request) # HttpResponseBadRequest#
# 403 (Forbidden) # HttpResponseForbidden#
# 404 (Not Found)  HttpResponseNotFound#
# 405 (Method Not Allowed) HttpResponseNotAllowed#
# 410 (Gone) HttpResponseGone#
# 500 (Internal Server Error) HttpResponseServerError