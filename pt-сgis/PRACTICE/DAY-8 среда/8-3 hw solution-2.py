class Thing:
    _attr = None
    def __init__(self, *args):
        _attr = dict(zip(self._attr, args))
        self.__dict__ = _attr

    def get_data(self):
        return filter(bool, self.__dict__.values())

class Table(Thing):
    _attr = ('name', 'price', 'weight', 'dims')


class ElBook(Thing):
    _attr = ('name', 'price', 'memory', 'frm')




table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data(), sep='\n')
print('-' * 20)
print(*book.get_data(), sep='\n')


table1 = Thing("Круглый", 100)
