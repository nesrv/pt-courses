class MyClass(object):
    ...

    def __str__(себяшка):
        return "я объекта класса"


# print(type(MyClass))
# print(type(int))
# print(type(str))


obj = MyClass()

print(type(obj))
print(obj)
print(hex(id(obj)))

print(isinstance(obj, MyClass))
print(isinstance(3, int))
print(isinstance(3.14, int))
print(isinstance(3.14, (int, float)))

