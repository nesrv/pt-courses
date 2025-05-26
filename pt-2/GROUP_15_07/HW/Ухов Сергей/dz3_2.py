# Car

class Car:
    __slots__=("_gas","_capacity","_gas_per_km","_ride")

    def __init__(self,capacity, gas_per_km):
        self._capacity=capacity
        self._gas_per_km=gas_per_km
        self._gas=0
        self._ride=0

    def fill(self,gas):
        if self._gas+gas>self._capacity:
            print(f"Бак полный, лишние литры: {(self._gas+gas)-self._capacity}")
            self._gas=self._capacity
        else:
            self._gas=+gas

    def ride(self,ride):
        if self._gas<self._gas_per_km*ride :
            raise ValueError("Не хватит бензина на такой пробег")
        self._ride=+ride
        self._gas=self._gas-self._gas_per_km*ride
        print(f"Проехали {ride} километров")

cr=Car(10,1)
cr.fill(10)

cr.ride(5)

cr.fill(10)

cr.ride(16)
