class Car:
    gas = 0
    capacity = 50
    gas_per_km = 0.075
    trip = 0

    def __init__(self, gas, capacity, gas_per_km, trip=0):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.trip = trip
    def fill(self, value):
        if self.gas + value <= self.capacity:
            self.gas += value
        else:
            print("слишком много бенза, не залить")

    def ride(self, length):
       if self.gas - (self.gas_per_km * length) > 0:
           self.gas = self.gas - (self.gas_per_km * length)
           self.trip += length
       else:
           print("недостаточно топлива чтобы проехать такую дистанцию")


car1 = Car(10, 50, 0.075)
car1.fill(40)
print(car1.gas)
car1.ride(650)
print(car1.gas)
print(car1.trip)