class Lamp:
    __slots__ = ('__state', '__floor', 'brand')

    def __init__(self, floor=0):
        self.__state = False  # private
        self.__floor = floor
        self.brand =  'Эра'


    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self,value):
        if type(value) == bool:
            self.__state = value
        else:
            print("Неправильно!")


    def get_floor(self):
        return self.__floor

    def set_floor(self, value):
        self.__floor = value

    floor = property(get_floor, set_floor)

    def __str__(self):
        return f'Я лампочка "{self.brand}" на {self.__floor} этаже'


lamp1 = Lamp(10)
lamp2 = Lamp(5)

lamp1.floor = 30
# lamp1.color = 'новый цвет'
lamp1.floor = "цоколь"
print(lamp1)
print(lamp2)


# print(lamp1.__dict__)
print(lamp1.__slots__)


