# массив - ?
# структура данных одного типа
# list - vektor
from pprint import pprint

from pprint import pp, pprint

lst1 = ["Москва", 1320, 5.8,
        ['1', "hello", 123],
        True, "Тверь", False]

lst2 = list('python')
print(lst2)

lst3 = [
    [1,2,4],
    [1,0,1],
    [0,0,1]
]

pp(lst3, width=20)

print('-' * 20)

pprint(lst3, width=20)
#
# print(lst1)
# print(id(lst1) , id(lst1[0]))
# print(lst1[0])
# print(lst1[3][1][0:3].upper())
# lst1[0] = "Питер"
# print(lst1)
# print(id(lst1), id(lst1[0]))


# print(id(lst2))
