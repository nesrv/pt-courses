# Декораторы функций
import time
from math import factorial
user = 'admin'


def test_time(func):
    def wrapper(*args):
        st = time.time()
        res = func(*args)
        dt = time.time()
        print(dt - st)
        return res
    return wrapper

@test_time
def fib(n):
    n1, n2 = 1, 1
    for i in range(2, n):
        n1, n2 = n2, n1 + n2
    return n2

@test_time
def some_func():
    return factorial(10**3)

print(fib(20_000))
print(some_func())
