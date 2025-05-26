# 1. Подбрасывание монеты

# Задание:
# ```
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),

import random


class Coin:
    side = None

    def __init__(self):
        self.side = None

    def flip(self) -> None:
        self.side = random.choice(['head', 'tail'])


# init vars
tails = int(0)
heads = int(0)
c = int(input("How many coins?"))

# 1. Создайте список из n-монеток
coins = list()
for i in range(0, c):
    coins.append(Coin)
# 2. Подбросьте(flip) все монетки... Отдельный цикл, т.к. создание и подброс разными пунктами
for i in coins:
    i.flip(i)
    match i.side:
        case 'head':
            heads += 1
        case 'tail':
            tails += 1
# 3. Выведите соотношение
print(f"Heads: {heads / c * 100:.2f}%")
print(f"Tails: {tails / c * 100:.2f}%")
