class Nikola:
    __slots__ = ['name', 'age']


    def __init__(self, name, age):

        if name == 'Николай':
            self.name = name
        else:
            self.name = f'Я не {name}, а Николай'
        self.age = age


person1 = Nikola('Иван', 31)
person2 = Nikola('Николай', 14)

print(person1.name)
print(person2.name)

# person1.surname = "Петров"

class Person:
    __slots__ = "_fio", "_old", "_job"

