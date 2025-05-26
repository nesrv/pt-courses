# Патерн моносостояние

class Point:
    __coords = {
        'x': 1,
        'y': 2
    }

    def __init__(self):
        self.__dict__ = self.__coords

    def __repr__(self):
        return self.print()

    # @staticmethod
    # def print():
    #    return f"Закрытые атрибуты: {Point.__coords}"

    @classmethod
    def print(cls):
        return f"Закрытые атрибуты: {cls.__coords}"

p = Point()

# print(p.__dict__)
#
# print(p.x)
p.x = 100

# print(p.__dict__)
print(p)
