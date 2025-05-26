# Наследование  от базовых классов


class Vector(list):
    def __str__(self):
        return ' '.join(map(str, self))

    def append(self):
       self.pop()


    def append_first(self, value):
        self.insert(0, value)

    # Разрешить сложение списка
    # со строкой и наоборот

    def __add__(self, other):
        return Vector(list.__add__(self, list(other))) #Константин

        # self.extend(other)
        # return self



v = Vector([1,'2','3'])
v.append()
v.append_first(100)
print(v)
v1 = v + 'python'
print(v1)

