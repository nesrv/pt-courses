class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point2D:
    __slots__ = ('__x', 'y')

    def __init__(self, x, y):
        self.__x = x
        self.y = y


    def get_private_x(self):
        return self.__x

p1 = Point(1, 2)
print (p1.x)

p1.y = 100
p1.z = 200

print (p1.y)


p2 = Point2D(100, 2)

print(p1.__dict__)
print(p2.__slots__)

print(p2.get_private_x())
