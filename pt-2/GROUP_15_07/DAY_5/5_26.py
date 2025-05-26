class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, eng):
        self.engine = eng

    def start(self):
        self.engine.start()
        print("Car started")


eng = Engine()

my_car = Car(eng)

my_car.start()