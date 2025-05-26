from math import hypot, dist

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

class Distance: # коробка функций
    PI = 3.14

    @staticmethod
    def get_dictance(p1, p2):
        return dist((p1.x, p1.y), (p2.x, p2.y))

    @staticmethod
    def get_len_lines(points):
        len_line = (Distance.get_dictance(points[i], points[i + 1])  for i in range(len(points) - 1))

        # for i in range(len(points) - 1):
        #     l = Distance.get_dictance(points[i], points[i + 1])
        #     len_line += l

        return sum(len_line)


    @staticmethod
    def cos2D():
        return 123

points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-16, 10),Point(-12, 0)]


len_l = Distance.get_len_lines(points)
print(len_l)




