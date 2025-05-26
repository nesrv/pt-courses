# doc strings

# написать ф-цию получение модуля числа
# решение в чат

def my_abs_airat(x):
    return (x ** 2) ** 0.5

def my_abs_andrew(x):
    return x if x >= 0 else -x

def my_abs_mickolay(x):
    if x < 0:
        x = x * -1
    return x

print(my_abs_airat(-10))
print(my_abs_airat(10))
print(my_abs_airat(-3.14))
print(my_abs_airat((0.1 + 0.1 + 0.1)))

print(my_abs_andrew(-10))
print(my_abs_andrew(10))
print(my_abs_andrew((0.3)))
