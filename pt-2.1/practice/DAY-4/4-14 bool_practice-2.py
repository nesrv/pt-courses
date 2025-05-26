from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def __ge__(self, other):
        return self.x + self.y >= self.x + other.y

    def __gt__(self, other):
        return self.x + self.y > self.x + other.y

p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1 <= p2)

lst = [p1,p2]

print(lst)

lst.sort()

print(lst)