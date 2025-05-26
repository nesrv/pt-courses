# __getitem__, __setitem__ и __delitem__


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if key > len(self.marks):
            self.marks.extend([None] * (key - len(self.marks) + 1))
        if isinstance(value, int):
            self.marks[key] = value
        else:
            raise TypeError("Оценка дб целым числом")

    def __delitem__(self, key):
        self.marks[key] = None


s1 = Student('Сергей', [5, 5, 3, 2, 5])

print(s1.marks[-1])
# print(s1[20])

s1[10] = 5

print(s1.marks)

del s1[2]

print(s1.marks)
