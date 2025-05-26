# __iter__ и __next__

# генераторы и итераторы


# r = range(10) # Какой тип данных ?
# r = "питон"
# r = [1,2,3]
#
# print(type(r))
# print(r.__iter__())
#
# for x in r:
#     print(x)

r = range(10**7)
r = iter(r)
print(r.__sizeof__())
print(type(r))
# print(*r)


# print(next(r))
# print(r.__next__())
#
