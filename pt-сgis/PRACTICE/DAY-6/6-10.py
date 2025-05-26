def f(x, y):
    if x == y:
        return 1
    if x > y or x == 15:
        return 0
    return f(x + 1, y) + f(x + 2, y)


path1 = f(3,9)
path2 = f(9,20)

print(path1)
print(path2)

total_path = path1 * path2

print(total_path)

