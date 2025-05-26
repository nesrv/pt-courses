class Car:

    def __init__(self, *args):
        self.gas, self.capacity, self.gas_per_km, self.mileage = args

    def fill(self, in_gas):
        print(f"Заправка {in_gas} литров...", end=" ")
        if in_gas + self.gas > self.capacity:
            print(f"Не вместилось {(in_gas + self.gas) - self.capacity} литров!", end=" ")
            self.gas = self.capacity
        else:
            self.gas += in_gas
        print("Машина заправлена")

    def __repr__(self):
        return (f'В баке: {self.gas} литров, '
                f'емкость бака: {self.capacity}, '
                f'расход: {self.gas_per_km} л/100 км, '
                f'пробег: {self.mileage} км')

    def ride(self, distance):
        print(f'Едем {distance} км...', end=' ')
        consumption = distance * self.gas_per_km / 100

        if consumption > self.gas:
            d = self.gas * 100 / self.gas_per_km
            print(f"Мы можем проехать только {d} км!")
            self.mileage += d
            self.gas = 0
        else:
            self.mileage += distance
            self.gas -= consumption
            print(f"Мы проехали {distance} км!")

    def __call__(self, distance):
        return self.ride(distance)

    def __add__(self, other):
        ...


car1 = Car(15, 45, 7.5, 25700)
print(car1)
car1.fill(55)
print(car1)
car1(700)
print(car1)
