import time
from os import getcwd, listdir

from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    data = {"header": "Лабиринт", "books" : ['Муму', "Онегин"]}
    return HttpResponse ("Мое первое приложение", context = data)


def about(requests, name, age):
    about_user = f'''
    <h2>О пользователе</h2>
    <p>Имя: {name}</p>
    <p>Возраст: {age}</p>
    '''
    return HttpResponse (about_user)


def contact(requests):
    return HttpResponse ("<h1>Обратная связь</h1>")

def current_time(requests):
    return HttpResponse(time.asctime())

def workdir(requests):
    return HttpResponse(getcwd())

def get_python_files(requests):
    info = []
    for file in listdir("."):
        info.append(file)
    info = "\n".join(info)
    return HttpResponse(info)

def calc(requests, x1, x2):
    return HttpResponse(str(x1 + x2))

def smart_calc(requests, data):
    return HttpResponse(eval(data))

def f404(requests, unknown_data):
    return HttpResponse(f'Страница {unknown_data} не существует', headers={'secret':'123'}, status=400)












