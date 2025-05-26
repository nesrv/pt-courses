# Подбрасывание монеты
import random

class Coin:
    def __init__(self):
        self.side=None

    def flip(self):
        s=random.randint(1,2)
        if s<2:
            self.side="heads"
        else:
            self.side="tails"
        # heads-орел/tails-решка

    def __repr__(self):
        return self.side

    def __call__(self, *args, **kwargs):
        return self.side

# кол-во монет
n_str = input("Количество монет:")
n=int(n_str)
coins=[Coin() for c in range(0,n,1)]

# подбрасываем монеты
for i in range(0,len(coins),1):
    coins[i].flip()

sum_heads=0
sum_tails=0
for i in range(0,len(coins),1):
    if coins[i].side=="heads":
        sum_heads+=1
    else:
        sum_tails+=1

# %%
print(f"heads: {(sum_heads/n)*100}%, tails: {(sum_tails/n)*100}% ")
#print(coins)
