from dataclasses import dataclass, field


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


@dataclass
class Point2D:
    x: int
    y: int
    lst: list = field(default_factory=list)

    def __post_init__(self):
        # print("сработал __post_init__")
        self.length = (self.x ** 2 + self.y ** 2) ** 0.5

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point2D(3, 4)
p4 = Point2D(3, 4)


print(p1)
print(p2)
print(p3)
print(p3.length)
print(p3.__dict__)
print(p1 == p2)
print(p3 == p4)
print(p1 > p2)