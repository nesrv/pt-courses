# ### Задача
# Допишите
# декоратор
# для
# цензурирования
# нелитературных
# слов
#
# ```python


def decorator(func):
    def prov(*args):
        if 'бяка' in args[0].lower():
            return 'Не пишите бяка!'
    return prov


@decorator
def censor(text):
    print("asfd")
    return f'текст {text} проверен'


print(censor('Hello'))
print(censor('Какая-то бяка'))


#
# ```
#
# Результат
# ```
# текст
# Hello
# проверен
# Не
# пишите
# бяка!
# ```