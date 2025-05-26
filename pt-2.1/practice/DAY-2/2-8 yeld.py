import time

mylist1 = [1, 2, 3, 4, 5]

# for x in mylist1:
#     print(x)
#
# mylist2 = [x*x for x in range(5)]
# # list comprehension (списковое включение) генератор списка(-)
# for x in mylist2:
#     print(x)
#
# mylist3 = (x*x for x in range(5)) # генератор

# for x in mylist3:
#     print(x)


# print(1, mylist1)
# print(2, *mylist2)

# print(next(mylist3))
# print(next(mylist3))
# print(next(mylist3))
#
# print(3, *mylist3)

mylist3 = (x * x for x in range(5))  # генератор

for i in mylist3:
    print(i)

print(mylist3)


def get_list():
    for x in mylist1:
        yield x


# print(*get_list())
#
# y = get_list()
#
# for i in y:
#     print(i)


# Бесконечный генератор последовательности Фиббоначи

def gen_fib(N):
    a, b = 1, 1
    for _ in range(N):
        yield a
        a, b = b, a + b


f = gen_fib(10)
while True:
    print(next(f))
    time.sleep(1)