def get_sum(total):
    s = 0
    for x in range(1, total+1):
        s += x
        yield s

# r = get_sum(5)
# print(*r)

from random import sample
from string import ascii_lowercase, ascii_uppercase, digits
chars = ascii_lowercase + ascii_uppercase + digits

# print(chars)

def passw_generator(n):
    while True:
        yield ''.join(sample(chars, n)) + "@mail.ru"


gen = passw_generator(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))