def test(n):
    a = 1
    b = 2
    c = 3
    for i in range(n):
        for j in range(n):
            a = i * i
            b = j * j
            c = i * j
    x = 4
    y = 5
    for i in range(n):
        x = a * b + 42
        y = c * i
    z = 100

# 3 + 3 * n ** 2 + 2 + 2 * n + 1


