from pprint import pprint

class Point:

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

    def change_color(self, color):
        self.color = color

p1 = Point(10, 20)
p2 = Point(12, 5, 'red')

print(p1.x, p1.y, p1.color)
print(p2.x, p2.y, p2.color)

points = []
for i in range(-1,1999,2):
    p = Point(i + 2, i + 2)
    points.append(p)

p3 = points[1]
print(p3.x, p3.y, p3.color)
p3.change_color('yellow')
print(p3.x, p3.y, p3.color)

