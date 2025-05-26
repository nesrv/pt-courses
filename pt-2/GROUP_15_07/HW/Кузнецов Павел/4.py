import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self):
        self.side = random.choice(['tails', 'heads'])

    @staticmethod
    def get_percent(coins):
        percent_tails = len([coin.side for coin in coins if coin.side == 'tails'])

        return percent_tails / len(coins) * 100


n = 1000

coins = [Coin() for _ in range(n)]

for c in coins:
    c.flip()

res = Coin.get_percent(coins)

print(res)
