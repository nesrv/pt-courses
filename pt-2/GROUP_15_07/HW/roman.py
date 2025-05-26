obscene_words = "слово1, слово2, слово3, слово4, слово5".split(', ')

# ---   решение с замыканием   -----------------------------------------
def correct(lst):
    def censor(text):
        ob_words = []
        for i in range(len(lst)):
            if lst[i] in text:
                ob_words.append(lst[i])
        return f'Не пишите {' '.join(ob_words)}!' if len(ob_words) else f'текст "{text}" проверен'
    return censor

is_correct = correct(obscene_words)
print(is_correct("Я люблю тебя жизнь!"))
print(is_correct("Я люблю, слово4, тебя жизнь, слово1!"))
print('-'*40)

# ---   решение с декоратором   ----------------------------------------
# передать obscene_words внутрь декоратора как с замыканием не получилось

def decorator(func):
    def wrapper(text):
        ob_words = []
        for i in range(len(obscene_words)):
            if obscene_words[i] in text:
                ob_words.append(obscene_words[i])
        return f'Не пишите {' '.join(ob_words)}!' if len(ob_words) else func(text)
    return wrapper

@decorator
def censor(text):
    return f'текст "{text}" проверен'

print(censor('Я люблю тебя жизнь!'))
print(censor('Я люблю, слово5, тебя жизнь, слово3!'))