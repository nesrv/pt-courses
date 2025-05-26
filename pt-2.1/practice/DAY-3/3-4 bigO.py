# bigO
import timeit


def palindrom_1(string):
    return string == string[::-1]


def palindrom_2(string):
    s1 = list(string)
    s2 = s1.copy()
    s2.reverse()
    if s1 == s2:
        return True
    return False


def palindrom_3(string):
    mid = len(string) // 2
    j = len(string) - 1
    for i in range(mid):
        if string[i] != string[j]:
            return False
        j -= 1
    return True


# start_time = timeit.default_timer()
# for _ in range(10**5):
#     palindrom_1('шалаш')
#
# print(timeit.default_timer() - start_time)

dt = timeit.Timer("palindrom_1('шалашшалашшалашшалаш')", "from __main__ import palindrom_1")
print(dt.timeit(10**5))

dt = timeit.Timer("palindrom_2('шалашшалашшалашшалаш')", "from __main__ import palindrom_2")
print(dt.timeit(10**5))

dt = timeit.Timer("palindrom_3('шалашшалашшалашшалаш')", "from __main__ import palindrom_3")
print(dt.timeit(10**5))

