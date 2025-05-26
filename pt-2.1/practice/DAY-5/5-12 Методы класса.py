
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x=0, y=0):
        self.int_validate(x,y)
        self.x = 0; self.y = 0
        if Vector.validate(x) and  Vector.validate(y):
            self.x = x
            self.y = y

    @staticmethod
    def int_validate(*args):
        for arg in args:
            if type(arg) != int:
                raise Exception("не целое число")
        return


    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def get_coord(self):
        return self.x, self.y


v = Vector(10.5, 50)

print (Vector.validate(400))

coord = v.get_coord()
print(coord)
