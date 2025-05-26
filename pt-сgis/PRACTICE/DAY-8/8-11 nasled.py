# наследование


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Я точка: {self.x} x {self.y}'


class Point3D(Point):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return f'{super().__repr__()} x {self.z}'

p = Point(1, 2)
print(p)

p3 = Point3D(10, 20, 30)

print(p3)

