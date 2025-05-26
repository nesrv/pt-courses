# ДЗ

stop_lists = {"слово1", "слово2", "слово3"}

def decorator(func):

    def prov(*args):
        text = set(args[0].split())
        if text & args[1]:
            return 'Не пишите плохие слова!'
        return func(*args)
    return prov


@decorator
def censor(text, st_lst):
    return f'текст {text} проверен'




text1 = "здесь присутствует слово1 и слово2"
text2 = "слово3 есть здесь"


print(censor('Hello', stop_lists))
print(censor(text1, stop_lists))
print(censor(text2, stop_lists))

