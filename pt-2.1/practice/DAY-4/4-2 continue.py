

class Lamp:
    brand = "Эра"
    count = 0

    def __init__(self, floor=0):
        self.__state = False
        self.__floor = floor
        Lamp.count+=1
        print(f'Создана лампочка № {Lamp.count} {Lamp.brand} на {floor} этаже ')

    def switch_on(self):
        if self.__state == False:
            print('Лампочку включили')

    def switch_off(self):
        if self.__state:
            print('Лампочку выключили')
            self.__state = False


    def __repr__(self): # str -> repr
        return f'я лампочка на {self.__floor} этаже'

    def get_floor(self):
        return self.__floor

    def set_floor(self, floor):
         self.__floor = floor


    floor = property(get_floor, set_floor)

    @property
    def state(self): #геттер
        return self.__state

    @state.setter
    def state(self, state):
         self.__state = state


lamp1 = Lamp(1)
lamp2 = Lamp(5)
lamp3 = Lamp(15)


lamp1.state = True
print (lamp1.state) # геттер
print(lamp2.__dict__['_Lamp__floor'])


def func():
    return 123

func.setter = 567
setattr(func, 'atr', "мир сошел с ума")

print(func.setter)
print(func.atr)

