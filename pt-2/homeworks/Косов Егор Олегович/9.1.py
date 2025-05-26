class Money:
    def __init__(self, money):
        self.money = money

    def __repr__(self):
        return f'Осталось {self.money} рублей'

    def show_how_much(self):
        return self.__repr__()


my_money = Money(100)
your_money = Money(1000)

print(my_money.show_how_much())
print(your_money.show_how_much())
print(my_money.__dict__)
print(your_money.__dict__)