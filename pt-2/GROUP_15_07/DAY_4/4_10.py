# reduce
from functools import reduce

# def add(x, y):
#     return x + y

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]

res1 = reduce(lambda summ, x: summ + x, numbers)
print(res1)

res2 = reduce(multiply, numbers, 1)
print(res2)