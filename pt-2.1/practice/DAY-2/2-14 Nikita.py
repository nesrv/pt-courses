
# map - list, str, dict, tuple


# t = 1, 2, 3, 4, 5
t ='hello python hello python hello python'
# t = list(map(float, t))
# t = list(map(lambda x: x ** x, t))
# t = list(map(lambda x: x ** x, t))
t = list(map(ord, t))

print(t.__sizeof__())

