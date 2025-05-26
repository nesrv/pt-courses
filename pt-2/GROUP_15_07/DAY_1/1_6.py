# Методы классов


class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x=1, y=0):
        print("вызов метода для", self)
        self.x = x
        self.y = y

    def get_coods(self):
        return f"Точка ({self.x}, {self.y})"

    # def __str__(self):
    #     return f"Точка ({self.x}, {self.y})"


# Point.set_coords(Point)

p1 = Point()
p1.set_coords(10,20)
# method = p1.set_coords  # объект ф-ция
# method - это что?
# method(10,20)
print(p1.__dict__)
print(p1.get_coods())

res = getattr(p1, 'get_coods') # объект ф-ция
print(res())

