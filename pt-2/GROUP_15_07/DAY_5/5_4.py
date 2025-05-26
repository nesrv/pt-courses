from time import time

def test_time(fn):
    def wrapper(*args, **kwargs):
        st = time()
        res = fn(*args, **kwargs)
        dt = time()
        print(f"Время работы: {dt - st} сек")
        return res
    return wrapper


@test_time
class MyFib:
    def fib(self, n):
        a, b = 1, 1
        i = 2
        while i < n:
            a, b = b, a + b
            i += 1
        return b


obj = MyFib()
print(obj.fib(10**4))
