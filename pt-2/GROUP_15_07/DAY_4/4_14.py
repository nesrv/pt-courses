from itertools import product

class pairMaker:

    def __call__(self, *args, **kwargs):
        self.pairs = tuple(product(args[0], args[1]))

    def __repr__(self):
        return str(self.pairs)

    def __len__(self):
        return len(self.pairs)

    def counter(self):
        return self.__len__()


men = ['Иван', 'Сергей']
women = ['Мария', 'Анна', 'Зоя']
#

pairs = pairMaker()
pairs(men, women)

print(pairs)  # ('Иван', 'Мария'), ('Иван', 'Анна'), ('Иван', 'Зоя'), ('Сергей', 'Мария'), ('Сергей', 'Анна'), ('Сергей', 'Зоя')
print(pairs.counter())
