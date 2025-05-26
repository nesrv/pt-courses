# Магический метод __len__ __bool__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Я точка ({self.x}, {self.y})'

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __bool__(self):
        return not self.x == self.y


p1 = Point(3, 4)
p2 = Point(0, 0)
p3 = Point(10, 10)
print(p1)
print(p2)
print(bool(p1))
print(bool(p2))
print(bool(p3))

print(len(p1))
print(len(p2))
print(len(p3))

if p1:
    print('объект p дает True')
else:
    print("объект p дает False")