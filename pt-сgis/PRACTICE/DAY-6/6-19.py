
class MyClass:
    color = 'red'
    circle = 2



a = MyClass()

print(a)

print(a.color)
print(a.circle)


MyClass.x = 'значение x'

print(a.__dict__)


a.y = "значение y"

print(a.x)
print(a.y)


setattr(MyClass, 'z', 100500)

print(MyClass.__dict__)

print(a.z)

print(getattr(a, 'z1', 'нет такого аттрибута'))
print(getattr(a, 'z2', None))