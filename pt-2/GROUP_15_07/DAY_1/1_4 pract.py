from pprint import pprint


class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Иван Иванов"
    views = 14356
    comments = 12


book1 = DataBase()
book2 = DataBase()


# print(DataBase.__dict__)
# print(book1.__dict__)
#
#
# book1.author = 'Тургенев'
#
# print(book1.__dict__)
# print(book2.__dict__)


# class Goods:
#     title = "Мороженое"
#     weight = 154
#     tp = "Еда"
#     price = 1024
# Goods.price =  2048
# setattr(Goods, "inflation", 100)
# print(Goods.__dict__)


class Car:
    ...

f = open("cars.txt", encoding='utf-8')

for row in f:
    attr, value = row.strip().split(": ")
    value = value.strip('".,')
    setattr(Car, attr, value)



from csv import reader, DictReader

class Dictionary:
    ...

f = open("attr.csv", newline="", encoding='utf-8')

attr = reader(f)

attr = list(attr)

for data in attr:
    attr, val = data
    setattr(Dictionary, attr, val)


pprint(Dictionary.__dict__)
# s = '''\t
# 3123
# 4234
# hello
# 3423
# '''.strip().splitlines()
#
# print('\t3123'.strip('\t'))







