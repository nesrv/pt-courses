


def decorator(func):
    def wrapper(text):
        if "бяка" in text:
            return "Не пишите бяка!"          
        return func(text)  
    return wrapper


@decorator
def censor(text):
    return f'текст {text} проверен'
    
print(censor('Hello'))
print(censor('Какая-то бяка'))    