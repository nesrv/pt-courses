# reduce
P = ['o', 'x', 'o', 'x', 'x', 'x', 'o', 'x', 'x']

res1 = [x == 'x' for x in P[0:3]]
res2 = [x == 'x' for x in P[3:6]]
res3 = [x == 'x' for x in P[6:]]

# print(all(res1))
# print(all(res2))
# print(all(res3))

# print(any(res1))

cities = 'Москва Питер Орел Сочи АНАПА'.split()
# все города с большой буквы

# print(*map(str.istitle, cities))
# print(*map(str.isupper, cities))

# cities = 'aнапа Анадырь Абакан Альметьевск'.split()
# все с буквы А

# print(*map(lambda w: w[0] == 'А', cities))
# print(*map(lambda s: s.startswith("А"), cities))


# string = '1 a1 фb2  c3 abc100 10 привет'
# # в строке нет русских букв
# # print(*map(str.isascii, string.split()))
#
# string = ',1 .! a1 фb2  c3 abc100 10'.split()
# print(string)
# # # в строке нет знаков препинания
# print(*map(str.isalnum, string))

cities = 'Анапа \nАнадырь \nАбакан Альметьевск'.split(' ')
# в строк нет спецсимволов
# print(*map(str.isprintable, cities))

quad = '10 25 49 81 100 200'.split()
quad = map(int, quad)
# в вывести через filter все полные квадраты

# res = filter(lambda x: (x**0.5)*(x**0.5) == x, quad)
# res = filter(lambda x: (x ** 0.5) ** 2 == x, quad)

res = filter(lambda x: (x ** 0.5) % 1 == 0, quad)

print(*res)
print(5.0 % 1)
print(9.0 % 1)

print((200 ** 0.5) ** 2)

