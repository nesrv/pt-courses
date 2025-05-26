class Point:
    COUNTER = 0


    def __init__(self,x,y, color ='black'):
        self.x=x
        self.y=y
        self.color=color
        Point.COUNTER += 1


points = []

for i in range(-1,1999,2):
    if int(Point.COUNTER)%2:
        p = Point(i + 2, i + 2, 'yellow')
    else:
        p = Point(i + 2, i + 2)
    print(p.__dict__)
    points.append(p.__dict__)

print(points)
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')
#
# print(p1.__dict__)
# print(p2.__dict__)


