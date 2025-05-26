# Анонимные функции. Сортировка коллекций по ключу

s = 'Hello Python from Russia'

s = s.split()

# как получить длины слов в коллекции?

# 5, 6, 4, 6

def get_len(word):
    return len(word)


print(list(map(get_len, s)))
print(*map(lambda word: len(word), s))
print(*map(len, s))

print(*map(max, s))  # ?

print(max(s, key=len))
print(sorted(s, key=len))

a = [4, 3, -10, 1, 7, 12]

a = sorted(a, key=lambda x: x % 2 == 0)

print(a)


lst = ['москва', "Москва",  "Тверь", "Смоленск", "Псков", "Рязань"]


lst = sorted(lst, key=lambda x: (x[-1], x[-2], ord(x[0])))

print(lst)






