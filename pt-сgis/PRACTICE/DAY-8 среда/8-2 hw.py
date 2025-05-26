class Thing:

    def __init__(self, *args):
        self.name, self.price, self.weight, self.dims, self.memory, self.frm = args

    def get_data(self):
        return filter(bool, self.__dict__.values())

class Table(Thing):
    def __init__(self, name, price, weight, dims, memory=None, frm=None):
        super().__init__(name, price, weight, dims, memory, frm)


class ElBook(Thing):
    def __init__(self, name, price, memory, frm, weight=None, dims=None):
        super().__init__(name, price, weight, dims, memory, frm)




table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data(), sep='\n')
print('-' * 20)
print(*book.get_data(), sep='\n')
