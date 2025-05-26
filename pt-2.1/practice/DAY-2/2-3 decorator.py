# Декораторы функций


def func_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args,  **kwargs)
    return wrapper

@func_decorator
def func(tag='div', title='заголовок', ):
    print(f'Вызов дек ф-ция с <{tag}> {title} </{tag}>')


# f = func_decorator(func)
# f(title="аргументами", tag='h1')


func(title="аргументами", tag='h1')
func()


