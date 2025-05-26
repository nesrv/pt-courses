
class MyClass:
    'мой класс'
    color = 'red'
    _circle = "секрет" # 3 степени защиты
    y = 100500



obj = MyClass()
obj2 = obj
obj2.color = 'green'

print(MyClass.__dict__)
print(obj.__dict__)

print(obj.color)
print(obj2.color)

# print(obj.__sizeof__())
#
# obj.y = 100
#
# print(obj.__dict__)
# print(obj.y)
#
# obj2 = MyClass

# print(obj2)
