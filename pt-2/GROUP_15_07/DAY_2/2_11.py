# Магические методы __len__, __abs__

class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return Point(*map(abs, self.__coords))

    def __repr__(self):
        return str(self.__coords)

p1= Point(-1,-200,3.14)

print(len(p1))

p1 = abs(p1)

print(p1)