import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        self.side = random.choice(['heads', 'tails'])
        return self.side


tails_c = 0
n = int(input("Введите количество монеток: "))

coins = [Coin() for i in range(n)]

for c in coins:
    c.flip()

if c.side == 'tails':
     tails_c += 1

print(f'{(tails_c/n)*100}% - решек, {((n-tails_c)/n)*100}% - орлов')