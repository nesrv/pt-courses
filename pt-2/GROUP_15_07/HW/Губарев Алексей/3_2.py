class Car:

    def __init__(self, gas, capacity, gas_per_km):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km

    def fill(self, volume):
        self.gas += volume
        if self.gas > self.capacity:
            print(f'Бензина залито больше на {self.gas - self.capacity} литров')
            self.gas = self.capacity
        print(f'В баке {self.gas} литров бензина')
    def ride(self, distance):
        self.probeg = 0

        if self.gas:
            possibly = self.gas / self.gas_per_km
            if (possibly - distance) > 0:
                self.gas -= self.gas_per_km * distance
                self.probeg += distance
                print(f'Проехали {distance} километров')
            else:
                self.gas -= self.gas_per_km * possibly
                self.probeg += distance
                print(f'Проехали {possibly} километров')


car1 = Car(10, 100, 1)

car1.fill(100)
car1.ride(50)