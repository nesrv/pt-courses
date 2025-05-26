#Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ...то есть, с увеличением на два для каждой новой точки.
#Каждый объект следует поместить в список points (по порядку). Для второго объекта в списке points укажите цвет yellow.

class Point():

    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.color = color

p1 = Point(10, 20)
p2 = Point(12, 5, 'red')

points = list()
for i in range(1, 2000, 2):
    if (i == 3):
        points.append(Point(i, i, 'yellow'))
    else:
        points.append(Point(i, i))

print(points[1].color)
print(points.__len__())
