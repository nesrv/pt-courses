class Point:

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []

for i in range(-1, 1999, 2):
    p = Point(i + 2, i + 2)
    points.append(p)

points[1].color = 'yellow'

print(points[1].color)