
# 2. Автомобиль
class Car:
    def __init__(self):
        self.gas = 0
        self.capacity = 0
        self.gas_per_km = 0
        self.mileage = 0

    def fill(self, gas_amount):
        t = self.gas + gas_amount
        if t < self.capacity:
            self.gas = t
            print(f"Fill {gas_amount}. {self.gas} litres in tank")
        else:
            print(f"Fill {self.capacity - self.gas} litres. Tank is full. Extra {t - self.capacity:.2f} litres")
            self.gas = self.capacity

    def ride(self, distance):
        tmp = self.gas_per_km * distance
        if tmp < self.gas:
            self.gas -= tmp
            print(f"Ride {distance} km. {self.gas} litres left")
            self.mileage += distance
        else:
            print(f"Ride only {self.gas / self.gas_per_km} km. Tank empty.")
            self.mileage += self.gas / self.gas_per_km
            self.gas = 0


car1 = Car()
car1.gas = 10
car1.capacity = 66
car1.gas_per_km = 0.1

car1.fill(50)
car1.ride(500)
print(car1.mileage)
car1.fill(50)
car1.ride(3000)
print(car1.mileage)
car1.fill(80)
car1.ride(200)
print(car1.mileage)