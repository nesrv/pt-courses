# lambda

def f1(a, b):
    f1.c = 3
    return a + b


# f2 = lambda a, b: a + b
### print(f1(2,2))
## print(f2(2,2))

# f1(2,2)
#
# f1.d = 10
# setattr(f1,"hello", "привет")
#
# print(f1.d)
# print(f1.c)
# print(f1.hello)
#
# print(f1.__dict__)


s = 'Hello Python123 From Russia Ryssia'.split()


def my_len(word):
    return len(word)


lambda_len = lambda word: len(word)

# lens_words = map(str.upper, s)
# lens_words = map(my_len, s)
# lens_words = map(lambda_len, s)
lens_words = map(f3 :=  lambda word: len(word), s)

lens_words = map(len, s)

print(f3("hello"))

print(*lens_words)

# print(max(s), ord('R'), ord('H'))

print(max(s, key=len))
