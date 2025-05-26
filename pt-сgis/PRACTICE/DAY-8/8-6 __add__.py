# Методы __add__, __sub__, __mul__

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        elif isinstance(other, int):
            return self.balance + other
        raise TypeError("неправильный тип данных")

    def __radd__(self, other):
        print('__radd__')
        return self + other


    def __repr__(self):
        return f'{self.name},{self.balance}'


user1 = BankAccount('Иван', 100)
user2 = BankAccount('Петр', 200)

user1.balance = user1.balance + 200
user1.balance = user1 + '1.234'
user1.balance = user1 + user2

user2 = user2 + user1

print(user1.balance)
print(user1)
print(user2)