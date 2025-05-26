## Домашка-1
### 1. класс Money
class Money:
    def __init__(self, money):
        self.__money = money
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money):
        self.__money = money

my_money = Money(100)
your_money = Money(1000)

print(my_money.money)
print(your_money.money)

your_money.money=1100
print(your_money.money)
