class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.describe_point()

    def describe_point(self):
        ch = self.x, self.y
        match ch:
            case 0, 0:
                desc = "в начале координат"
            case _,0:
                desc = "на оси х"
            case 0, 1:
                desc = "на оси y"
            case x,y if x == y:
                desc = f"по линии x = y = {x}"
            case x,y:
                desc = f"Точка с координами {x} и {y}"

        return desc


p0 = Point2D(0, 0)  # в нач координат
p1 = Point2D(5, 0)  # на оси х
p2 = Point2D(0, 3)
p3 = Point2D(-3, -3)
p4 = Point2D(1, 2)

print(p0.describe_point())
print(p1.describe_point())
print(p2.describe_point())
print(p3.describe_point())
print(p4.describe_point())


print('\n\n', p4)