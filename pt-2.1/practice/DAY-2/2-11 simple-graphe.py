def get_paths(x, y):
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    else:
        return get_paths(x + 1, y) + get_paths(x + 2, y)


print(get_paths(3, 9) * get_paths(9, 20))


def get_fib(n):
    if n == 1 or n == 2:
        return 1
    return get_fib(n - 2) + get_fib(n - 1)

print(get_fib(8))