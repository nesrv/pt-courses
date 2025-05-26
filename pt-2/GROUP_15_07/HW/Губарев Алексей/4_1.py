# Допишите декоратор для цензурирования нелитературных слов
def decorator(func):
    def wrapper(text):
        for word in text.split():
            if word == 'бяка':
                print("Не надо писать всякое")
            else:
                func(text)
    return wrapper


@decorator
def censor(text):
    return f'текст {text} проверен'


print(censor('Hello'))
print("=" * 30)
print(censor('Какая-то бяка'))
