# ПАВЕЛ

#ЗАДАНИЕ 1
# import json


# class Programmer:
#     ...

#     def has_attribute(self, attribute):
#         return print(hasattr(self, attribute))

# file = open("practice/DAY-3/attr.json", encoding='utf-8')
# dictJson = json.load(file)

# for key, value in dictJson.items():
#     setattr(Programmer,key,value)

# p1 = Programmer()

# print(hasattr(p1, "job")) #1
# p1.has_attribute("job") #2

# print('job' in Programmer.__dict__) #3


#ЗАДАНИЕ 2

# class Soda:
#     def __init__(self, additive = None):
#         self.additive = additive
#     def show_my_drink(self):
#         print(f"Газировка и {self.additive}" if self.additive else "Обычная газировка")

# soda1 = Soda("Малина")
# soda2 = Soda()
# soda1.show_my_drink()
# soda2.show_my_drink()

class Soda:
    def __init__(self, supplement=None):
        if supplement:
            self.supplement = supplement

    def show_my_drink(self) -> str:
        if hasattr(self, 'supplement'):
            return f'Газировка и {self.supplement}'
        return f'Обычная газировка.'


Soda1 = Soda('Колокольчик')
print(Soda1.show_my_drink())
Soda2 = Soda()
print(Soda2.show_my_drink())


#ЗАДАНИЕ 3

class Point:
    id = None
    def __init__(self, x, y, color = "black"):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self) -> str:
        return f"Point: x = {self.x}, y = {self.y}, color = {self.color}"
    
class Point:
    color = 'black'
    def __init__(self, x=0, y=0, color=None):
        self.x = x
        self.y = y
        if color:
            self.color = color

    def get_data(self):
        return (self.x, self.y, self.color)


p1 = Point(10, 20)
p2 = Point(12, 5, 'red')

print(p1.__dict__)
print(p2.__dict__)

pnt = 10
points = []
cunt = 0

points = [Point((i*2)+1, (i*2)+1, 'yellow').get_data() if i == 1 else Point((i*2)+1, (i*2)+1).get_data() for i in range(pnt)]

print(points)


p1 = Point(10, 20)
p2 = Point(12, 5, 'red')

points = []

# counter = 1
# for x in range(1000):
#     points.append(Point(counter, counter))
#     counter += 2

# [points.append(Point(x,x) if x == 1 else Point(points[-1].x+2,points[-1].y+2)) for x in range(1,1000)]

# points[1].color = 'yellow'
# print(points[1].__dict__)

cnt = 20
cnt *= 2
example = (Point(*val) for val in enumerate(range(1, cnt + 1, 2), 1))

print(next(example))
print(next(example))