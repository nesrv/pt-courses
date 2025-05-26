from time import asctime
from json import dumps


user = "user"


def access(func):
    def wrapper(*args, **kwargs):
        if user == "admin":
            func(*args, **kwargs)
        else:
            print("доступ запрещен")

    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        d = {
            "Имя-функции": func.__name__,
            "Произвольные аргументы" : args,
            "Именованные аргументы": kwargs,
            "Возвращаемое значение": func(*args, **kwargs),
            "Время и дата вызова функции": asctime()
        }
        print(dumps(d,ensure_ascii=False, indent=4))
        return ...
    return wrapper

@access
@logger
def add_numbers(a, b, comment=""):
    return a + b



add_numbers(10,20, comment="ф-ция сложения")