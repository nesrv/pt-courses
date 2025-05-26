# Магические методы __iter__ и __next__


r = range(5)

r = iter(r)
print(next(r))
print(next(r))
print(next(r))

print(*r)

for x in range(0.5,2,0.5):
    print(x, end=' ')