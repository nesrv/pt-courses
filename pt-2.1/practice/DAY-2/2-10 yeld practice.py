from string import ascii_lowercase, ascii_uppercase
from random import sample

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"



def gen_passw(N):
    while True:
        five_passw = (''.join(sample(chars, N)) +'\n' for _ in range(5))
        yield five_passw


f = gen_passw(10)

print(*next(f))


