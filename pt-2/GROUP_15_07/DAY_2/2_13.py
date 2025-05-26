from math import hypot
# __eq__() – для равенства ==
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return int(hypot(self.x, self.y))

    def __repr__(self):
        return f'Точка ({self.x} {self.y})'

    def __gt__(self, other): # le
        return len(self) > len(other)

    # def __eq__(self, other):
    #      return self.x == other.x

# Дан список точек

points = [Point(12, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
#
len_points = {p: len(p) for p in points}
# print(len_points)
#
# print(max(len_points))
# print(sorted(len_points))

p1 = Point(12, 17)
p2 = Point(12, 7)
print(p1 == p2)
# Найдите длину ломаной линии

