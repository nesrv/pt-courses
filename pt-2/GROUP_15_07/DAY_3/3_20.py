class Animal:

    def __init__(self, name, old):
        self.name, self.old = name, old
        self.info = f'{self.name} : {self.old}'

    def get_info(self):
        return self.info


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color, self.weight = color, weight
        self.info += f' {self.color} : {self.weight}'


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed, self.size = breed, size
        self.info += f' {self.breed} : {self.size}'


cat = Cat('кот', 4, 'black', 2.25)
print(cat.get_info())

dog = Dog('собака', 4, "бульдог", (2, 2))
print(dog.get_info())
