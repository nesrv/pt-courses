from itertools import product, permutations
from random import shuffle, sample

all_list = [[1, 3, 4], [6, 7, 9], [8, 10, 5]]

res = product(*all_list)

class CardDeck:

    def __init__(self):
        self._suits = '♠♣♦♥'
        self._ranks = [*range(2, 11), "J", "Q", "K", "A"]
        self._deck = list(product(self._ranks, self._suits))
        self._index = 0

    def deck_shuffle(self):
        shuffle(self._deck)

    def __next__(self):
        if self._index < len(self._deck):
            card = self._deck[self._index]
            self._index += 1
            return card
        raise StopIteration("Колода закончилась")

    def __iter__(self):
        return self

    def get_cards(self, n):
        # выдать n карт сверху колоды

        return [self._deck.pop() for _ in range(n)]

    def get_random_cards(self, n):
        return sample(self._deck, n)
        # как достать n карт случайных (не сверху!)


deck = CardDeck()
# deck.deck_shuffle()

cards_five = deck.get_cards(3)
print(cards_five)

cards_rnd = deck.get_random_cards(3)
print(*cards_rnd)


# print(next(deck))
# print(next(deck))
# print(next(deck))
#
# for card in deck:
#     print(card)