from math import prod

# Методы списков

lst = [10, 1, 20, 3, 4]

# len, sorted (ф-ция), sort(метод - точечная нотация)

print(1, len(lst))

lst1 = sorted(lst)

print(2, lst1)

lst.sort(reverse=True)
print(3, lst)

lst.reverse()

print(4, lst)

lst = lst[::-1]

print(5, lst)

print(6, sum(lst))

print(7, sum(lst) / len(lst))

print(8, prod(lst))

print(max(lst))

print(20 in lst)

lst *= 2

print(lst)
print(lst[-3:])

lst[-3:] = [0, 0, 0]
print(lst)

lst[-3:] = [100] * 10

print(lst)
