# Режимы доступа public, private, protected. Сеттеры и геттеры
# private
class Lamp:
    BRAND = "ЭРА"
    __COUNTER = 0

    def __init__(self, floor=0):
        self.__state = False
        self.__floor = floor
        Lamp.__COUNTER += 1
        self.__count = Lamp.__COUNTER

    def __repr__(self):
        return f'Я лампочка № {self.__count} на {self.__floor} этаже'
    #
    # def get_count_lamp(self):
    #     return Lamp.__COUNTER

    @classmethod
    def get_count_lamp(cls):
        return cls.__COUNTER
    # способ 1
    # def __get_floor(self):
    #     return self.__floor
    #
    # def __set_floor(self, floor):
    #     self.__floor = floor
    #
    # floor = property(__get_floor, __set_floor)

    # способ 2
    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, floor):
        self.__floor = floor

l1 = Lamp(10)
l2 = Lamp(2)

print(l1.floor)
l1.floor = 200
print(l1.floor)
print(Lamp.get_count_lamp())
print(Lamp.__dict__)
Lamp._Lamp__COUNTER = 200
print(Lamp._Lamp__COUNTER)