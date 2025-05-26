# Именованные кортежи

from collections import namedtuple

user = namedtuple("юзер", "имя возраст статус")

Ivan = user(имя="Иван", возраст=20, статус="программист")

print(Ivan.имя)
# print(Ivan.__dir__())
# print(Ivan.__slots__)

Point = namedtuple("Point", ["x", "y", "z"])

p = Point(4, 7, 10)
print("x:", p.x)
print("x:", p.y)



Engine = namedtuple('Engine', ['type', 'cylinders'])
Car = namedtuple('Car', ['make', 'model', 'year', 'engine'])
engine_instance = Engine(type='1.5L', cylinders=4)

car_instance = Car(make='Honda', model='City', year=2020, engine=engine_instance)

print(car_instance.make)
print(car_instance.engine)
print(car_instance.engine.cylinders)