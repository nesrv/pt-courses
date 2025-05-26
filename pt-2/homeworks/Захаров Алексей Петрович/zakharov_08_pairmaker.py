# task 4
from itertools import *


class PairMaker:

    def __init__(self, men=None, women=None):
        self.men = men
        self.women = women
        self.pairs = list()

    def __call__(self, lst1, lst2):
        self.pairs = list(product(lst1, lst2))

    def __repr__(self):
        return str(self.pairs)

    def counter(self):
        return len(self.pairs)


men = ['Иван', 'Сергей']
women = ['Мария', 'Анна', 'Зоя']

pairs = PairMaker()
pairs(men, women)

print(pairs)
# ('Иван', 'Мария'), ('Иван', 'Анна'), ('Иван', 'Зоя'), ('Сергей', 'Мария'), ('Сергей', 'Анна'), ('Сергей', 'Зоя')
print(pairs.counter())
# 6
