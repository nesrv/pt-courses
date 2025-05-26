# Асинхронное поведение на генераторах
import time


def counter():
    c = 0
    while True:
        print('счетчик = ', c)
        c += 1
        yield


def printer():
    c = 0
    while True:
        if c % 3 == 0:
            print('печать ...', c)
        c += 1
        yield

c = counter()
p = printer()

while True:
    next(c)
    time.sleep(1)
    next(p)
    time.sleep(1)

