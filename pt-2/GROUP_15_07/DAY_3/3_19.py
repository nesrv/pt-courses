# Атрибуты private и protected при наследовании

class Point:
    def __init__(self, x, y):
        self.__x = x if self._verify_coords(x) else 0
        self.__y = y if self._verify_coords(y) else 0

    def __repr__(self):
        return f'{self.__x} x {self.__y}'

    def move_by(self, x, y):
        self.__x += x
        self.__y += y
    # @private #  accessify
    @staticmethod
    def _verify_coords( coord): # protected доступен нашим детям
        return 0 < coord < 100

class Point3D(Point):

    def __init__(self, x, y, z):
        self.__z = z if super()._verify_coords(z) else 0
        super().__init__(x,y)

    def move_by(self, x, y, z):
        self.__z += z
        super().move_by(x,y)

    def __repr__(self):
        return f'{super().__repr__()} x {self.__z}'

p = Point(-1, 2)
print(p)

p3d = Point3D(10, 20, 30)
print(p3d)

p3d.move_by(10,10,10)

print(Point._verify_coords(-10))


