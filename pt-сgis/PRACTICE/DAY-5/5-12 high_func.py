# Функции высшего порядка

# map lambda  filter reduce


def is_divide_3(x):
    return x % 3 == 0


lst = [1, 2, 5, 10, 22, 33, 102]

res1 = filter(lambda x: x % 2, lst)
res2 = filter(lambda x: x % 2 == 0, lst)

# все числа, заканчивающиеся на 2?

res3 = filter(lambda x: x % 10 == 2, lst)

res4 = filter(is_divide_3, lst)


print(*res1)

print(*res2)

print(*res3)

print(*res4)