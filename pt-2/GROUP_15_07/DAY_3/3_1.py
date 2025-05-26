# Магический метод __bool__
from math import hypot


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        return self.x == self.y

    def __len__(self): # eq
        print("__len__")
        return int(hypot(self.x, self.y))

p = Point(3, 4)
print(bool(p))

p1 = Point(1, 2)
print(bool(p1))

if p1:
    print("объект дает true")
else:
    print("объект дает false")