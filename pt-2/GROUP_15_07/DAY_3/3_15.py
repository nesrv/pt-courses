# Наследование

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def __repr__(self):
        return f'{self.x} x {self.y}'

    def move_by(self, x, y):
        self.x += x
        self.y += y

class Mixin:

    def __init__(self):
        print("запись логов")

    def printer(self):
        print("я класс миксин")

class Point3D(Point, Mixin):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def move_by(self, x, y, z):
        self.z += z
        super().move_by(x, y)
        # Point.move_by(self, x, y) # под капотом


    def __repr__(self):
        return f'{super().__repr__()} x {self.z}'


p1 = Point(1, 2)
p2 = Point3D(3, 4, 5)
p1.move_by(10, 10)
p2.move_by(10, 10, 10)
print(p1)

print(p2)
print(p2.printer())

print(Point3D.__mro__)
# print(issubclass(Point3D, Point))
