stop_words = {'слово1', 'слово2', 'бяка'}

def decorator(func):
    def wrapper(*args):
        args = args[0].split()
        if stop_words & set(args):
            print("проверка не пройдена")
            return stop_words & set(args)
        else:
            print("проверка пройдена")
            return func(args)

    return wrapper


@decorator
def censor(text):
    return f'текст {text} проверен'


print(censor('Hello'))
print(censor('Hello world'))
print(censor('Какая-то бяка'))
print(censor('слово1 слово2'))
