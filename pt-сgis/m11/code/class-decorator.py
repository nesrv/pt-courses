# декорирование классом 

from time import time

class TestTime:

    def __init__(self, func):
        self.func = func

    def __call__(self,n):
        st = time()
        self.func(n)
        dt = time()
        print(f"Время работы: {dt - st} сек")



@TestTime
def fib(n):
    a, b = 1, 1
    i = 2
    while i < n:
        a, b = b, a + b
        i += 1
    return b



print(fib(10**4))


from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    job: str

anne = Person(first_name="Anne",
              last_name="Smith",
              age=40,
              job="software engineer",)


# print(anne)