# @property
# @dataclass
# @staticmethod
# @classmethod

from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10 ** 5)

# @lru_cache(None)
def F(n):
    if n == 1:
        return 1
    else:
        return n * F(n - 1)


# for i in range(2, 3000):
#     F(i)

print(F(2024) / F(2000))