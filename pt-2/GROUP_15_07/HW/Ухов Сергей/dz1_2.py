## Домашка-1
## 2.  класс Point
# Для второго объекта в списке points укажите цвет `yellow`.

class Point:
    def __init__(self, x,y, color="black"):
        self.x=x
        self.y=y
        self.color=color
    def info(self):
        return f'point x={self.x} y={self.y}  color={self.color}'

points = []
for i in range(-1,1999,2):
    p = Point(i + 2, i + 2)
    points.append(p)

points[2].color="yellow"
print(points[2].info())

