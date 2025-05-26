class Money:
    def __init__(self, money):
        self.money = money

    def __str__(self):
        return f"Деньги : {self.money}"

my_money = Money(100)
your_money = Money(1000)


print(my_money)