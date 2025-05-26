# Магический метод __getitem__, __setitem__ и __delitem__

# __getitem__(self, item) – получение значения по ключу item;
# __setitem__(self, key, value) – запись значения value по ключу key;
# __delitem__(self, key) – удаление элемента по ключу key.

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
        if not isinstance(key, int) and key < 0:
            raise IndexError("Индекс дб целым полож числом")
        if key > len(self.marks):
            self.marks.extend([None] * (key - len(self.marks) + 1))
            self.marks[key] = value
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) and key < 0:
            raise IndexError("Индекс дб целым полож числом")
        del self.marks[key]

s1 = Student('Сергей', [5, 5, 3, 2, 5])

print(s1[0])
s1[9] = 2
print(s1[9])
print(s1.marks)

del s1[0]
