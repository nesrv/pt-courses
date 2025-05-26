class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def enter(person):
    name = person.name
    age = person.age

    match name, age:
        case name, age:
            print(f"{name}, пришел")

    match person:
        case person.name, person.age:
            print(...)

        case Person(name=person.name, age=person.age) if age < 18:
            print(f"{name}, доступ запрещен")

        case Person(name=name, age=age) if age < 22:
            print(f"{name}, доступ ограничен")

        case Person(name=name):
            print(f"{name}, добро пожаловать!")


enter(Person("Tom", 37))
enter(Person("Sam", 12))
enter(Person("Bob", 20))
