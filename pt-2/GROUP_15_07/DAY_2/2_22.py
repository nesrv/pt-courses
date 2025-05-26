class Nikola:
    #__slots__ = ('_name', '_age')

    # def __new__(cls, *args, **kwargs):
    #     print("__new__")

    def __init__(self, name, age):
        if name == "Николай":
            self._name = name
        else:
            self._name = f'Я не {name}, а Николай'


# оно преобразуется в “Я не Максим, а Николай”.

person1 = Nikola('Иван', 31)
print(person1._name)

person2 = Nikola('Николай', 14)
print(person2._name)

person2.first_name = "Иванович"