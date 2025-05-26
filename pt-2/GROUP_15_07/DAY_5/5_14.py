def f(x, y):
    if x == y:

        return 1
    if x > y:
        return 0
    print("prev", x)
    return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)


res = f(3,6)

print(res)