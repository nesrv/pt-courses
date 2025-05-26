# Сложность алгоритмов BIG 0
import timeit
from timeit import timeit, Timer


def counter_virus_1(n, t): # каждые 3 часа делится пополам
    i = 3
    while i <= t:
        n *= 2
        i += 3
    return n


def counter_virus_2(n, t):
    return n * 2 ** (t//3)



r1 = counter_virus_1(1, 12)
r2 = counter_virus_2(1, 12)

print(r1)
print(r2)

# t1 = Timer("capitalisation1(100, 15, 5000)", "from __main__ import capitalisation1")
# t2 = Timer("capitalisation2(100, 15, 5000)", "from __main__ import capitalisation2")
#
#
# print(t1.timeit(number=10**4))
# print(t2.timeit(number=10**4))
