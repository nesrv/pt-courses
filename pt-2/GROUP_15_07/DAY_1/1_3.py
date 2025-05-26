# setattr getattr delattr hasatrib
from pprint import pprint


class Point:
    color = 'red'
    circle = 2

p1 = Point() #  ?
p1.lst = [1,2,2]

print(id(Point), id(p1))


pprint(Point.__dict__)
pprint(p1.__dict__)

setattr(p1, 'x', 1)

pprint(p1.__dict__)

x = getattr(p1,"x1", False)
x = getattr(p1,"x1", "нет такого аттрибута")
print(x)

# delattr(p1, 'x')

if hasattr(p1, 'x'):
    print(p1.x)
else:
    print("не нашел такого аттрибута")

p1.x, p1.y= 10,20

print(p1.__dict__)

