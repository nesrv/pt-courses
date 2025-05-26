# __iter__ и __next__
# генераторы и итераторы

class IterColumn:

    def __init__(self, lst, column):
        self.lst = lst
        self.column = column
        self.row = -1

    def __next__(self):
        if self.row < len(self.lst) - 1:
            self.row += 1
            return self.lst[self.row][self.column]
        else:
            raise StopIteration

    def __iter__(self):
        self.row =-1
        return self

lst = [
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
]

it = IterColumn(lst, 1)

print(next(it))
print(next(it))
print(next(it))

print('-' * 20)
for x in it:
    print(x)