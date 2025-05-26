from pprint import pprint

from accessify import private, protected

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
    @protected
    @classmethod
    def __get_count_lamp(cls):
        return cls.__COUNTER

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, floor):
        self.__floor = floor

l1 = Lamp(10)
l2 = Lamp(2)
pprint(Lamp.__dict__)

# Lamp._Lamp__COUNTER = 200
# print(Lamp._Lamp__COUNTER)