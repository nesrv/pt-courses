# task 5
from itertools import *
all_list = [[1, 3, 4], [6, 7, 9], [8, 10, 5]]

res = list(product(*all_list))
print(res)
print(len(res))
