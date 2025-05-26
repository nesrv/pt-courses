import itertools
class Thing:

    id = itertools.count()

    def __init__(self, name = None, price = None, weight = None, dims = None, memory = None, frm = None):
        self.id : int = next(Thing.id)
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm

    def get_data(self):
        return (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)

class Table(Thing):
    def __init__(self, name = None, price = None, weight = None, dims = None):
        super().__init__(name, price, weight, dims)

class ElBook(Thing):
    def __init__(self, name = None, price = None, memory = None, frm = None):
        super().__init__(name, price, memory, frm)

th = Thing('ololo', 100500)

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(table.get_data())
print(book.get_data())
print(th.get_data())

#table = Table(name,price,weight,dims)
#book = ElBook(name,price,memory,frm)