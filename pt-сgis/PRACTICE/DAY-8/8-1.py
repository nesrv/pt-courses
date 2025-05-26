class Lamp:
    brand = 'Эра'
    count = 0

    def __init__(self, floor=0):
        self.__state = False  # private
        self.__floor = floor
        Lamp.count += 1
        self.count = Lamp.count

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self,value):
        if type(value) == bool:
            self.__state = value
        else:
            print("Неправильно!")


    def switch_on(self):
        if self.__state == False:
            self.__state = True

    def switch_off(self):
        if self.__state == True:
            self.__state = False

    def get_floor(self):
        return self.__floor

    def set_floor(self, value):
        self.__floor = value

    floor = property(get_floor, set_floor)

    def __str__(self):
        return f'Я лампочка № {self.count} "{Lamp.brand}" на {self.__floor} этаже'


lamp1 = Lamp(10)
lamp2 = Lamp(5)

lamp1.floor = 30
lamp1.state = 'абракадабра'
lamp1.floor = "цоколь"


print(lamp1.floor)


