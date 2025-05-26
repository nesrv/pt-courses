
stop_list = {'слово1', 'слово2', 'бяка'}

def decorator(func):
    def wrapper(*args):
        words = set(args[0].split())
        check = words & stop_list
        if check:
            return f"Не прошло проверку слова: {check}"
        return func(*args)
    return wrapper



@decorator
def censor(text):
    return f'текст {text} проверен'


print(censor('Hello'))

print(censor('Какая-то бяка'))

print(censor('слово1 слово2'))


