import random

class Coin:
    def __init__(self):
        self.side = None  # Монетка находится в неопределенном состоянии

    def flip(self) -> None:
        """
        Подбрасывание монетки. heads-орел/tails-решка
        """
        self.side = random.choice(['heads', 'tails'])  # Случайным образом определяем сторону

def main():

    n = int(input("Введите количество монеток: "))


    coins = [Coin() for _ in range(n)]


    for coin in coins:
        coin.flip()


    heads_count = sum(1 for coin in coins if coin.side == 'heads')
    tails_count = n - heads_count


    heads_percentage = (heads_count / n) * 100
    tails_percentage = (tails_count / n) * 100

    print(f"Орлы: {heads_percentage:.2f}%")
    print(f"Решки: {tails_percentage:.2f}%")

if __name__ == "__main__":
    main()
