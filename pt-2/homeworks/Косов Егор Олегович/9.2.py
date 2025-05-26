class Point:
    def __init__(self, x,y, color = 'black'):
        self.x = x
        self.y = y
        self.color = color

points = []
for i in range (-1, 1999, 2):
    p = Point(i+2, i+2)
    if i==1:
        setattr(p, 'color', 'yellow')
    else:
        pass
    points.append(p)
    print(p.color)
    print(p.x, p.y)