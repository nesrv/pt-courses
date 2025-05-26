def fib(n=20):
    a = b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


gen_fib = fib(5)

print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))

print(*gen_fib)
