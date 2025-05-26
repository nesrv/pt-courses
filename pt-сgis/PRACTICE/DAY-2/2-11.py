# Цикл for

# vowels = "ауоыэяюёие"
#
# for i, letter in enumerate(vowels, 1):
#     if letter == 'ы':
#         continue
#     print(i, letter, sep=' - ')
#
# else:
#     print("всё ок")
#
# print('конец цикла')
# range - диапазон

from math import prod

# r = range(1, 10, 2)
# print(r)
# print(sum(r))
# print(max(r))
# print(len(r))
# print(5 in r)
# print(*r)
# print(prod(r))

# for x in r:
#     print(x, end=' ')

# for x in range(20,-1, -1):
#     if x % 3 == 0:
#      print(x)

# Гражданин 1 января открыл счет в банке,
# вложив 1000 руб. Каждый год размер вклада
# увеличивается на 15% от имеющейся суммы.
# Определить сумму вклада через n лет


s = 1000 # рублей
n = 10 # лет

# while n > 0:
#     s = s * 1.15
#     n -= 1

for i in range(n):
    print(i, round(s,2))
    s = s * 1.15

print(s)









