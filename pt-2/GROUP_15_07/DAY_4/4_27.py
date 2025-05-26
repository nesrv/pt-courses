def func_show(func):
    def wrapper(*args):
        print(f'Площадь прямоугольника: {func(*args)}')

    return wrapper


@func_show
def get_sq(a, b):
    return a * b



def show_menu(func):
    def wrapper(*args):
        s = ''
        for i, x in enumerate(func(*args), 1):
            s += f'{i}. {x}\n'
        return s
    return wrapper


@show_menu
def get_menu(string):
    return string.split()


s = "пунктА пунктБ пунктВ"

res = get_menu(s)

print(res)
