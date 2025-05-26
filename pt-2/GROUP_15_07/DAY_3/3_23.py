class Furniture:
    _attr = None
    def __init__(self, *args):
        attr = dict(zip(self._attr, args))
        self.__dict__ = attr

    def get_attrs(self):
        return tuple(self.__dict__.values())

class Closet(Furniture):
    _attr = ('_name', '_weight', '_tp', '_doors')

class Chair (Furniture):
    _attr = ('_name', '_weight', '_height')

class Table (Furniture):
    _attr = ('_name', '_weight', '_height', '_square')




cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
print(chair.get_attrs())

# print(cl.__dict__)
# print(chair.__dict__)