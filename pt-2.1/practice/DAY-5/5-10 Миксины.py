# Миксины (классы-примеси)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()


    def __repr__(self):
        return f'Я точка'


class MixinLog:
    _ID = 0
    def __init__(self):
        MixinLog._ID +=1
        print('вызов миксина', MixinLog._ID,  super().__repr__())
        super().__init__()

class Network:
    def __init__(self):
        print('Отправка данных по сети')



class Point3D(Point, MixinLog, Network ):
    def __init__(self, x, y, z):
        self.__z = z
        super().__init__(x, y)

    def __repr__(self):
        return f'Я 3D-точка'


p3 = Point3D(1, 2 ,3)
p4 = Point3D(1, 2 ,3)
p2 = Point(1, 2)

print(p2)
print(p3)

# print(*Point3D.__mro__, sep='\n')