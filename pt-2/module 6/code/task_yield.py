from itertools import cycle
from math import factorial
from string import ascii_lowercase, ascii_uppercase
from random import choice, seed
from string import *
from random import *



def get_sum(N):
    summ = 0
    for i in range(1, N+1):
        summ += i
        yield summ


chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"


def get_pass1(N):
    yield (choice(chars) for _ in range(N))


def get_pass2(N):
    return (choice(chars) for _ in range(N))


print(*next(get_pass1(5)), sep='')

print(*get_pass2(5), sep='')

# ========================================================


chars = ascii_lowercase + ascii_uppercase

seed(1)


def generator(N):
    yield ''.join(choice(chars) for _ in range(N)) + '@mail.ru'


N = int(input())

for _ in range(5):
    print(next(generator(N)))


# ========================================================
# Вильсон

def get_simple(n=3):
    while True:
        if not (factorial(n - 1) + 1) % n != 0:
            yield n
        n += 2


gen = get_simple()
print(2, end=' ')
for _ in range(19):
    print(next(gen), end=' ')

##
from itertools import cycle

def infinite(lst, iterations):
    result = ''
    iter_lst = cycle(lst)
    if lst:
        for symbol in range(iterations):
            result += str(next(iter_lst))
    return result


# Тесты
print(infinite([2, 5, 8], 7))
print(infinite([], 1000))
print(infinite([7], 4))


