class Point:
    def __init__(self, x, y, color = 'black'):
        self.x = x
        self.y = y
        self.color = color

    def set_color(self, color):
        self.color = color

p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
print(p1.__dict__)
print(p2.__dict__)

points = []
N = 1 + (1000-1)*2
print(f'N={N}')
for i in range(1,N+1,2):
    pi = Point(i, i)
    # if i == 3 :
    #     pi.color = 'yellow'
    points.append(pi)

points[1].set_color('yellow')
# печать - для проверки
for p in points:
    print(p.__dict__, end="")
