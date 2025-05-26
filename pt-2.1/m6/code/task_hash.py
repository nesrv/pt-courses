class BookStudy:
    def __init__(self, name, author, year):
        self.name, self.author, self.year = name, author, year

    def __hash__(self):
        return hash((self.name, self.author))


    def __repr__(self):
        return f'{self.name}-{self.author}'


    def __eq__(self, other):
        return hash(self) == hash(other)

s = '''
Отцы и дети; Тургенев; 2024
Война и мир; Толстой; 2001
Братья Карамазовы; Достоевский; 1954
Война и мир; Толстой; 2022
Братья Карамазовы; Достоевский; 2024
Война и мир; Толстой; 1972
'''.strip().splitlines()


lst = [BookStudy(*book.split('; ')) for book in s]
print(*lst, sep='\n')
print('='*40)
res = set(lst)
print(*res, sep='\n')



