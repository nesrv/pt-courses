class Money:


    def __init__(self, Money1):
        print("сработал init")
        self.money = int(Money1)


my_money = Money(100)
your_money = Money(1000)

print(my_money.money)
print(your_money.money)

print(your_money.money-my_money.money)


