from pprint import pprint


class Point:
    color = 'red'
    circle = 2

    def __str__(self):
        return f' Я точка {self.color}'

 
print(Point.__doc__)
print(Point.color)

Point.color = "black"

print(Point.color)

pprint(Point.__dict__)

p1 = Point()

print(p1.__dict__)

print(p1.color)
print(p1.circle)

p1.color = "pink"

print(p1.__dict__)

del p1.color

print(p1.color)

print(p1.__dict__)
