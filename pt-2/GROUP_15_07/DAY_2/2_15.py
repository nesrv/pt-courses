# Методы __add__, __sub__, __mul__

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            balance = self.balance + other.balance
        elif isinstance(other, (int, float)):
            balance = self.balance + other
        else:
            raise TypeError("Нужно вводить числа")
        return BankAccount(self.name, balance)

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return f'{self.name} : {self.balance}'

user1 = BankAccount('Иван', 100)
user2 = BankAccount('Петр', 200)
user3 = BankAccount('Дима', 146)
user1.balance = user1.balance + 300

user1 = user1 + user2 + user3
print(user1)

# user1 = 200 + user1
#
# user1 = user1 + user2
# user1 = user1 + 125.5
#
# print(user1)
