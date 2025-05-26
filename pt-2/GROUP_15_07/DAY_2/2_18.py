class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y

        if isinstance(other, (tuple, list)):
            x = self.x + other[0]
            y = self.y + other[1]

        return Point(x, y)

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return f'Точка ({self.x} {self.y})'

# Как сложить (вычесть, перемножить) две точки?

p1 = Point(2, 7)
p2 = Point(2, 7)
print(p1)
p3 = p1 + p2
print(p3)
p4 = p3 + (10,20)
print(p4)
p5 =  (10,20) + p4
print(p5)