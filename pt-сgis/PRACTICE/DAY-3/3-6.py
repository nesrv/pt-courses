from math import prod

# Методы списков - count, index


l1 = ['1', '2', 'abc', '1', 20, 20, 'abc', 20, 'abc', 'abc']


# print(l1.count('1'))
# # print(l1.count(20))
#
# print(l1.index('abc'))
# print(l1)
#
# # while 'abc' in l1:
# #     l1.remove('abc')
#
# print(l1)
#
# for x in l1:
#     if x == 'abc':
#         l1.remove('abc')
#
# print(l1)

i = 0
while i < len(l1):
    i = l1.index('abc',i)
    print(i)
    i += 1

# print(l1.index('abc',0))
# print(l1.index('abc',3))
# print(l1.index('abc',7))





