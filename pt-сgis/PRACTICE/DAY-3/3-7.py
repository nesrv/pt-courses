from math import prod
from pprint import pprint

# list comprehension

l1 = [x ** 2 for x in range(10)]

l2 = [x ** 2 for x in range(10) if x % 2]
print(l2)

# s = '1 5 25 31 45'
# s = s.split()
# print(s)
# l3 = [int(x) // 5 for x in s]
# print(l3)
#
# l4 = [f'{x} - нечетное' if x % 2 else f'{x}-четное' for x in l3]
# print(l4)

matrix = [
    [
        f'{i} * {j} = {i * j}' for i in range(1, 5)
    ]
    for j in range(1, 5)
    ]

print(*matrix, sep='\n')
