# __add__, __sub__, __mul__


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        return self.balance + other

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return f'{self.name}, {self.balance}'


user1 = BankAccount('Иван', 100)
user2 = BankAccount('Петр', 200)

print(1, user1)

user1.balance = user1.balance + 300
user1 = user1 + 300  # +
print(2, user1)
user1 = user1 + user2
print(3, user1)


