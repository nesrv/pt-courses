# __getitem__, __setitem__ и __delitem__


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        return self.marks[item]

    def __setitem__(self, key, value):
        if type(value) == int and 2 <= value <= 5:
            if key > len(self.marks):
                self.marks.extend([None] * (key - len(self.marks) + 1))
            self.marks[key] = value
        else:

            raise ValueError("оценка дб числом от 2 до 5")

    def __delitem__(self, key):
        self.marks[key] = None


s1 = Student('Сергей', [5, 5, 3, 2, 5])

print(s1.marks[0])
print(s1[0])

s1[3] = 4
s1[8] = 2

print(s1[:])
del s1[0]
print(s1[:])
