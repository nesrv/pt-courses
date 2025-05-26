# map + lambda

s = '10 20 5 1'
s = s.split()
# s = [int(x) for x in s]

s = list(map(int, s))
print(s)

def my_func(x):
    return x + 100

s = list(map(lambda x: x ** 2, s))
print(s)

s = list(map(my_func, s))

print(s)

s = 'Hello Python from Russia ZZZ Абракадабра'
s = s.split()

# lens_words = map(lambda word: len(word), s)

words = list(map(lambda word: word.upper(), s))
words = ['Тверь', 'Псков', 'Москва', 'Рязань', 'Смоленск']

max_word = max(words, key=len)

print(max_word)

# sorted_words = sorted(words)
# sorted_words = sorted(words, key=len)
sorted_words = sorted(words, key=lambda w : (w[-1], w[-2]))
print(sorted_words)