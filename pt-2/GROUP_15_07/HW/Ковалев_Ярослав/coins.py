import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(['heads', 'tails'])

n = int(input("Введите количество монеток: "))
coins = [Coin() for _ in range(n)]

for coin in coins:
    coin.flip()

heads_count = sum(1 for coin in coins if coin.side == 'heads')
tails_count = n - heads_count

heads_percent = (heads_count / n) * 100
tails_percent = (tails_count / n) * 100

print(f"Процент орлов: {heads_percent}%")
print(f"Процент решек: {tails_percent}%")