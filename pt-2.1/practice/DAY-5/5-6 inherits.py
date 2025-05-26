class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Я точка: {self.x} x {self.y}'

    def move_to(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point):

    def __init__(self, x, y, z):
        self.z = z
        super().__init__(x, y)

    def __repr__(self):
        return f'{super().__repr__()} x {self.z}'

    def move_to(self, x, y, z):
        super().move_to(x, y)
        self.z = z


p = Point(1, 2)
p.move_to(100, 200)
print(p)

p3 = Point3D(10, 20, 30)
p3.move_to(100, 200, 300)
print(p3)
