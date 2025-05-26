# class Thing:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __repr__(self):
#         return f"Thing: {self.__dict__}"
#
#
# t = Thing("Учебник по Python", 100, 1024)
# print(t)


from dataclasses import dataclass, field
from math import hypot


@dataclass
class Point:
    x: int
    y: int
    lst: list = field(default_factory=list)
    distance: float = field(init=False)


    def __post_init__(self):
        print('__post_init__')
        self.distance = hypot(self.x, self.y, 0,0)

p1 = Point(3,4)
p2 = Point(1,2)
# p1.lst.append('123')
print(p1.distance)
print(p1)
print(p1.__dict__)
p1.x = 100
print(p1)




