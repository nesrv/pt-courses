# наследование от базовых классов


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


    def append(self):
        self.pop()

    def append_first(self, value):
        self.insert(0, value)

# Как переопределить метод append,
# реализовав в нем не добавление элементов,
# как по умолчанию, а удаление последнего
# элемента

a = Vector()
a.extend("132143")
a.extend((1,2, 'end'))

print(a)
a.append()
a.append_first('append_first')
print(a)