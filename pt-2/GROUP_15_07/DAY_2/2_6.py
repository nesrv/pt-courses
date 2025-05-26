# call + ф-ция filter


# def f(n):
#     return n % 10
#
# f1 = lambda n : n % 10

x = [10,5,20,30, 11]

y = filter(lambda n : n % 10 == 0, x)

print(*y) # ?