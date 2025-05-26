
# кортеж tuple
# неизменяемый тип данных

c = (1,2,3, 'hello', [1,2,3], (1,2,3))
l = [1,2,3, 'hello', [1,2,3], (1,2,3)]
print(c)
print(l)

print(c.__sizeof__())
print(l.__sizeof__())

l[0] = '123'
c = ('123',) + c[1:]
print(c)
print(l)
a = 1,2,"hello","hello","hello"
print(a)

# append -
# insert -
# extend -
# c[1] = -

# len, in, index, sum, min, max, count, find

print(a.index('hello'))
print(a.count('hello'))

b = tuple(['питон', 'змея'])

print(b)