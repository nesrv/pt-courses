from itertools import cycle
from time import sleep

colors = ["red", "yellow", "green"]
def get_color():
    for color in cycle(colors):
        print(color)
        yield


def counter():
    c = 0
    while True:
        print("работает счетчик", c)
        c += 1
        yield


def printer():
    c = 0
    while True:
        if c % 2:
            print("печатаю ...")
        c += 1
        yield

c = counter()
p = printer()
c1 = get_color()

while True:
    next(c)
    sleep(0.5)
    next(p)
    sleep(0.5)
    next(c1)
