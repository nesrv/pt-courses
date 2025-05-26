import timeit

s = 1000  # рублей
percent = 20  # процентов
ages = 10  # на 10 лет


# найти капитализацию ?
# bigO

def capital_1(s, percent, ages):
    for age in range(ages):
        s += s * percent / 100
    return s

# bigO = 2n
# bigO = O(n)


def capital_2(s, percent, ages):
    return s * (1 + percent/ 100) ** ages

# bigO = 1 +  1 + 1 +1 = 4
# bigO = O(1)

# start_time = timeit.default_timer()
#
# for i in range(10 ** 4):
#     c1 = capital_1(1000, 20, 1000)
#
# print(timeit.default_timer() - start_time)
#
# start_time = timeit.default_timer()
#
# for i in range(10 ** 4):
#     c2 = capital_2(1000, 20, 1000)
#
# print(timeit.default_timer() - start_time)

t1 = timeit.Timer("capital_1(1000, 20, 1000)", "from __main__ import capital_1")
t2 = timeit.Timer("capital_2(1000, 20, 1000)", "from __main__ import capital_2")


print(t1.timeit(1000))
print(t2.timeit(1000))