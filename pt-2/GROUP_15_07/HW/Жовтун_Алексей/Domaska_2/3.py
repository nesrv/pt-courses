class Nikola:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        if name == "Николай":
            self.name = name
        else:
            self.name = f'Я не {name}, а Николай'


# оно преобразуется в “Я не Максим, а Николай”.

person1 = Nikola('Алексей', 44)
print(person1.name)

person2 = Nikola('Николай', 14)
print(person2.name)

# person2.first_name = "Иванович"
# print(person2.first_name)