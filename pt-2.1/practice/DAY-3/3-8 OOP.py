
class MyClass:
    'мой класс'
    color = 'red'
    __circle = "секрет" # 3 степени защиты

print(type(MyClass))

MyClass.color='black'
MyClass.x = 100

print(*MyClass.__dict__.items(), sep='\n')
# print(MyClass.__dict__['__doc__'])
# print(MyClass.__dict__['color'])
# print(MyClass.__dict__['_MyClass__circle'])
# print(MyClass.color)
# print(MyClass.x)
# print(MyClass.__circle)

setattr(MyClass, 'y', 200)
print(getattr(MyClass, 'z', None))
print(MyClass.y)

print(*MyClass.__dict__.items(), sep='\n')
# del MyClass.y
if hasattr(MyClass, 'y1'):
    delattr(MyClass, 'y1')

print(*MyClass.__dict__.items(), sep='\n')
