# Сложность алгоритмов BIG 0
import timeit
from timeit import timeit, Timer


def palindrom_1(string):
    return string == string[::-1]


def palindrom_2(string):
    s1 = list(string)
    s2 = s1.copy()
    s2.reverse()
    return s1 == s2


def palindrom_3(string):
    mid = len(string) // 2
    j = len(string) - 1
    for i in range(mid):
        if string[i] != string[j]:
            return False
        j -= 1
    return True


# st = timeit.default_timer()
# for _ in range(10 ** 5):
#     r1 = palindrom_1("шалаш")
#
# print(timeit.default_timer() - st)

t1 = Timer("palindrom_1('шалаш')", "from __main__ import palindrom_1")
t2 = Timer("palindrom_2('шалаш')", "from __main__ import palindrom_2")
t3 = Timer("palindrom_3('шалаш')", "from __main__ import palindrom_3")

print(t1.timeit(number=10**6))
print(t2.timeit(number=10**6))
print(t3.timeit(number=10**6))
