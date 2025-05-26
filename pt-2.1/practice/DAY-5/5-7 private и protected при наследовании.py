# Атрибуты private и protected при наследовании


class Point:
    _xx = 'я защищенный'
    def __init__(self, x, y):

        self.__x = x
        self.__y = y

    def __repr__(self):
        return f'Я точка: {self.__x} x {self.__y}'

    def move_by(self, x, y):
        self.__x += x
        self.__y += y


class Point3D(Point):
    def __init__(self, x, y, z):
        self.__z = z
        super().__init__(x, y)

    def move_by(self, x, y, z):
        self.__z = + z
        super().move_by(x, y)

    def __repr__(self):
        # print (super().__xxx)
        s = super().__repr__()
        return f'{s} x {self.__z}'

p = Point(1, 2)
print(p)
p3d = Point3D(10, 20, 30)
print(p3d)

print(Point._xx)
# p3d.move_by(50, 50, 50)
# print(p3d)
# p.move_by(50, 50)
# print(p)