#Task 1
bs='''
Отцы и дети; Тургенев; 2024
Война и мир; Толстой; 2001
Братья Карамазовы; Достоевский; 1954
Война и мир; Толстой; 2022
Братья Карамазовы; Достоевский; 2024
Война и мир; Толстой; 1972
'''.strip().splitlines()
class BookStudy:
    def __init__(self, name, author,year):
        self.name = name
        self.author = author
        self.year = year

    def __repr__(self):
        return f'Книга: "{self.name}" автор: {self.author}'

    def __eq__(self, other):
        return self.name == other.name and self.author == other.author


    def __hash__(self):
        return hash((self.name, self.author))
    
bs=[BookStudy(*book.split('; ')) for book in bs]
print(*set(bs), sep='\n')