
# декоратор для цензурирования нелитературных слов

def decorator(fun):
    dict=["бяка","хайп","фу"] # нелитературные слова
    def wrapper(text):
        fun(text, dict)
    return wrapper

@decorator
def censor(text, dict):
    words=text.split()
    rez=""
    if list(set(words) & set(dict)).__len__()>0:
        rez=f"В тексте '{text}' есть нелитературные слова"
    else:
        rez=f"Текст '{text}' проверен"
    return print(rez)

tx1="собака бяка"
censor(tx1)

tx2="сказал фу"
censor(tx2)

tx3="больше всякого разного"
censor(tx3)