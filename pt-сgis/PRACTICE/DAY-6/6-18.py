
class MyClass:
    color = 'red'
    circle = 2


# print(MyClass.circle)
# print(MyClass.color)
#
# print(*MyClass.__dict__.items(), sep='\n')
# print(MyClass.__dict__['circle'])


a = MyClass()

print(a)

print(a.color)
print(a.circle)

print(a.__dict__)
print(MyClass.__dict__)