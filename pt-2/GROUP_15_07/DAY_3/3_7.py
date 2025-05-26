# Магический метод __new__. Singleton

class Point:

    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для " + repr(cls))
        return super().__new__(cls)


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print("вызов __init__ ", repr(self))

    def __repr__(self):
        return f'Точка ({self.x} {self.y})'


pt = Point(1, 2)

print(pt)