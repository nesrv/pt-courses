# Наследование от базовых классов


class Tuple(tuple):
    def __add__(self, other):
        # решение в чат
        # Константин
        # Роман
        # return Tuple(tuple.__add__(self, tuple(other)))
        # return tuple(list(self) + list(other)) # +/-
        # return Tuple((*self, *other)) # +
        return Tuple(tuple(self) + tuple(other))

t = Tuple([1, 2, 3])
t = t + "Python"

print(t)

t = (t + "Python") + "ООП"

print(t)
