# Конструктор (инстансе)
# Инициализатор init


class Point:
    color = 'red'
    circle = 2

    def __init__(self, x,y):
        print("сработал __init__", x,y)
        self.x = x
        self.y = y


    def __del__(self):
        print(self)
        print("сработал финализатор")

p1 = Point(1,2)
print(p1.__dict__)
print(p1.x, p1.color)

del p1

# print(p1)