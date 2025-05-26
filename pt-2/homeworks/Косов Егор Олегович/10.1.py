import random
class Coin:
    sides = ['heads' , 'tails']
    def __init__(self):
        self.side = None

    def flip(self):
        lst = ['heads', 'tails']
        self.side = random.choice(self.sides)
        return self.side


    def __repr__(self):
        return self.side

n = 5
kopeyki = [Coin() for i in range(n)]
results: tuple = [coin.flip() for coin in kopeyki]
comp_results = results.count('heads')/results.count('tails')
print(comp_results)