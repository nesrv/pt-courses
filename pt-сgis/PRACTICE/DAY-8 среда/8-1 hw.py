import json

from time import asctime

def logger(func):
    def wrapper(*args, **kwargs):
        result = {
            "Имя-функции" : func.__name__,
            "Произвольные аргументы" : list(args),
            "Именованные аргументы" : kwargs,
            "Возвращаемое значение" : func(*args),
            "Время и дата вызова функции" :  asctime()
        }
        return json.dumps(result, ensure_ascii=False, indent=4)
    return wrapper


@logger
def add_numbers(a, b, точность=2):
    return a + b



@logger
def some_func(a, b):
    return a ** b


print(add_numbers(2,2))
print(some_func(2,2))