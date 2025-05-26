class SuperPoint:
    '''суперкласс'''


class Point(SuperPoint):
    ''' аннотация'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Точка ({self.x},{self.y})'


p1 = Point(2, 7)
print(Point.__mro__)
print(issubclass(Point, SuperPoint))
print(issubclass(list, object))
print(issubclass(int, object))
print(p1.__dict__)
print(p1.__class__.__name__)
print(dir(Point))
print(p1)