# __call__
from time import time
from math import factorial


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1):
        self.__counter += step
        print("работаю как функция", self.__counter)


c = Counter()


class TestTime:

    def __init__(self, func):
        self.func = func

    def __call__(self, n):
        st = time()
        self.func(n)
        dt = time()
        print(f"Время работы: {dt - st} сек")


@TestTime
def fact(n):
    return factorial(n)

@TestTime
def fib(n):
    n1, n2 = 1, 1
    for i in range(2, n):
        n1, n2 = n2, n1 + n2
    return n2

print(fact(10_000))
print(fib(200_000))