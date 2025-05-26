
# Декораторы функций


def decorator(func):
    def wrapper(*args):
        func(*args)
    return wrapper

@decorator
def some_func(title, tag='div'):
    print(f"<{tag}> {title} </{tag}>")


some_func("Вызов функции some_func", 'h1')
some_func("Вызов функции 2")
# some_func_2()
