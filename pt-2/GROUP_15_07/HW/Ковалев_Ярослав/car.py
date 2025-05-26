class Car:
    def __init__(self, gas=0, capacity=50, gas_per_km=5):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km
        self.kmcount = 0

    def fill(self, liters):
        if self.gas + liters > self.capacity:
            extra_liters = self.gas + liters - self.capacity
            self.gas = self.capacity
            print(f"Бак заполнен. Лишние {extra_liters} литров.")
        else:
            self.gas += liters

    def __add__(self, liters):
        self.fill(liters)
        return self

    def ride(self, km):
        if self.gas < km / self.gas_per_km:
            distance = self.gas * self.gas_per_km
            self.gas = 0
            print(f"Едем {distance} км. Бензин закончился.")
            self.kmcount += distance
        else:
            self.gas -= km / self.gas_per_km
            print(f"Проехали {km} км.")
            self.kmcount += km

car1 = Car()
car1.fill(5)  # Бак заполнен. Лишние 5 литров
print(car1.gas)  # 50

car1.fill(60)
print(car1.gas)  # 50 (не добавилось, т.к. бак уже полный)

car1.ride(150)
print(f"Одометр: {car1.kmcount} км.")

car1 += 60
print(car1.gas)