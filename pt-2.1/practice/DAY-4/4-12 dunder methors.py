bool(123)  # 1
bool(-1)  # 1
bool(0)  # 0
bool("python")  # 1
bool("")  # 0
bool([])  # 0
bool(None)  # 0


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        return self.x == self.y

    def __len__(self):
        return False if self.x == 0 and self.y == 0 else True

p = Point(3, 3)
p1 = Point(0, 1)

print(bool(p))
print(bool(p1))

if p1:
    print("Координаты равны")
else:
    print("объект p дает False")