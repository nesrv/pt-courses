# Yield
# __next__ = генератор
# __iter__ = итератором (for)

# mylist1 = [1, 2, 3]
# for i in mylist1 :
#    print(i)
#
# mylist2 = [x*x for x in range(3)]
# for i in mylist2 :
#    print(i)
#
#
# mylist3 = (x*x for x in range(3))
# for i in mylist3 :
#    print(i)
#
# print(mylist1)
# print(mylist2)
# print(*mylist3)


def get_list1():
   for x in (1, 2, 3):
      yield x


def get_list2():
   return (x for x in (1, 2, 3))

y1 = get_list1()
y2 = get_list2()

print(type(y1))
print(type(y2))






