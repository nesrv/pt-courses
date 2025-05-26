# Магические методы  hash

hash(123)
hash("Python")
h1 = hash((1, 2, 3))
h2 = hash((1, 2, 3))
# hash([1, 2, 3])
#
# print(h1)
# print(h2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'точка ({ self.x},{ self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)

print(hash(p1))
print(hash(p2))

print(hash(p1) == hash(p2))

d = {
    p1:'p1',
    p2:'p2',

}
d[p1] = 'т1'
d[p2] = 'т2'


print('вывод=', d)

