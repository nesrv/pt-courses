import random


# 1. Подбрасывание монетки
class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(['tails', 'heads'])


n = int(input("Введите n: "))
coins = [Coin() for _ in range(n)]
for c in coins:
    c.flip()

tails = sum(1 for c in coins if c.side == 'tails')
print(f'{(tails / n) * 100}% - tails, {((n - tails) / n) * 100}% - heads')


# 2. Автомобиль
class Car:
    def __init__(self, gas: int, capacity: int, gas_per_km: int):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.mileage = 0

    def fill(self, x: int):
        self.gas += x
        if self.gas > self.capacity:
            print(f'Слишком много бензина, {self.gas - self.capacity} лишних литров')
            self.gas = self.capacity
        print(f'В баке теперь {self.gas} литров бензина')

    def ride(self, km: int):
        need_gas = self.gas_per_km * km
        drove_km = km if need_gas <= self.gas else self.gas / self.gas_per_km
        self.gas -= drove_km * self.gas_per_km
        self.mileage += drove_km
        print(f'Проехали {drove_km} км')
        print(f'Пробег = {self.mileage} км')


car = Car(100, 150, 2)
car.fill(5)
car.ride(50)
car.ride(10)


# Интернет-магазин
class Thing:
    NEXT_ID = 0

    def __init__(self, name: str, price: float):
        self.id = Thing.NEXT_ID
        Thing.NEXT_ID += 1
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    def get_data(self):
        return self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm


class Table(Thing):
    def __init__(self, name: str, price: float, weight: float, dims: tuple[int, int, int]):
        super().__init__(name=name, price=price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name: str, price: float, memory: int, frm: str):
        super().__init__(name=name, price=price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
