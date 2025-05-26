def f(x, y):
    if x == y:
        return 1
    if x > y or x == 15:
        return 0
    return f(x + 1, y) + f(x + 2, y)


res1 = f(3,9)
res2 = f(9,20)

print(res1 * res2)