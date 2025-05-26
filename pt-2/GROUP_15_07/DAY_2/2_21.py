# коллекция slots
# PY Python 3.12.4

from timeit import timeit
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x +=1
        del self.y
        self.y = 0

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def calc(self):
        self.x +=1
        del self.y
        self.y = 0

p1 = Point(1,2)
p2 = Point2D(3,4)

t1 = timeit(p1.calc)
t2 = timeit(p2.calc)

print(t1)
print(t2)
print(p1.__sizeof__())
print(p2.__sizeof__())

# print(p1.__dict__)
# print(p2.__slots__)
# print(p2.z)
# print(p2.max_l)
# p2.x = 500
# del p2.x
# p2.x = 1500
# print(p2.x)

# 0.770097117
# 0.581365135
# 16
# 16