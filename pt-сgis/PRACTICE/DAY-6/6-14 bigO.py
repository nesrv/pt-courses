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

# bigO = 3 + 3 * n^2 + 2 + 2*n + 1
# 3n^2 + 2n
# 3n^2
# n^2 O(n^2)

