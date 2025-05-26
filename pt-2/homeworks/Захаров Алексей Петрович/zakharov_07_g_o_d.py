from itertools import *
# task 3
s = "ГОД"
res = product(s, repeat=6)
c = 0
for i in res:
    if i[0] != "О":
        c += 1
print(c)
