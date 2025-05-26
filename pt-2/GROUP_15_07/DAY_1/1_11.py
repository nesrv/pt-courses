# Режимы доступа public, private, protected. Сеттеры и геттеры

# private
class Lamp:
    BRAND = "ЭРА"
    COUNTER = 1

    def __init__(self, floor=0):
        self.__state = False
        self.__floor = floor
        self.__count = Lamp.COUNTER
        Lamp.COUNTER += 1

    def switch_on(self):
        if self.__state == False:
            print("Лампу включили")
            self.__state = True

    def switch_off(self):
        if self.__state:
            print("Лампу выключили")
            self.__state = False

    def __str__(self):
        return f'Я лампочка № {self.__count} на {self.__floor} этаже'

    def __repr__(self):
        return self.__str__()
        # return str(self)


l1 = Lamp(10)
l2 = Lamp(2)

# print(isinstance(l1, Lamp))

print(l1.switch_on())
print(l2.switch_on())
# print(l1.switch_off())
#
# # print(l1, l2)
#
# lst = [l1, l2]
#
# print(lst)

print(l1.__dict__)
print(l1._Lamp__state)
print(l1._Lamp__floor)