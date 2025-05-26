# Сложность алгоритмов BIG 0
import timeit
from timeit import timeit, Timer


def capitalisation1(capital, percent, year):
    return capital * (1 + percent/100) ** year


def capitalisation2(capital, percent, year):
    for _ in range(year):
        capital += capital * percent / 100
    return capital


# r1 = capitalisation1(1000, 10, 15)
# r2 = capitalisation2(1000, 10, 15)
#
# print(r1)
# print(r2)


t1 = Timer("capitalisation1(100, 15, 5000)", "from __main__ import capitalisation1")
t2 = Timer("capitalisation2(100, 15, 5000)", "from __main__ import capitalisation2")


print(t1.timeit(number=10**4))
print(t2.timeit(number=10**4))
