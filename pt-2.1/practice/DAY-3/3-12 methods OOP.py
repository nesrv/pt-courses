# конструктор (инициализатор) инстанс
# __init__ магический (dunder) метод

class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        print('сработал конструктор')
        self.x = x
        self.y = y

    def __str__(self):
        return f'Я точка ({self.x}, {self.y})'

    def __del__(self):
        print ('сработал финализатор')


p1 = Point(1,2)
print(p1.__dict__)

p2 = Point()
print(p2.__dict__)

print(p1)

p2.z = 100
print(p2.__dict__)

