# eq и hash

# хешируемые и нехешируемые типы данных
# что это?

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # сделал класс нехешируемым
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'Я точка ({self.x} {self.y})'


p1 = Point(1, 2)  # хэши одинаковые ?
p2 = Point(1, 2)

print(hash(p1))
print(hash(p2))

print(p1 == p2)

d = {}

d[p1] = "точка 1"
d[p2] = "точка 2"

print(d)
