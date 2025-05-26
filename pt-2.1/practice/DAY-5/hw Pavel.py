#ЗАДАНИЕ 1



# text = """
# Отцы и дети; Тургенев; 2024
# Война и мир; Толстой; 2001
# Братья Карамазовы; Достоевский; 1954
# Война и мир; Толстой; 2022
# Братья Карамазовы; Достоевский; 2024
# Война и мир; Толстой; 1972
# """.strip().replace('"','').splitlines()

# class BookStudy:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def __repr__(self):
#         return f'Книга: {self.title} автор: {self.author}'
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
#     def __hash__(self):
#         return hash((self.title.lower(), self.author.lower()))


# # bs = BookStudy("name", "author", "year")

# books = [BookStudy(*row.split("; ")) for row in text]

# print(*books, sep="\n")
# print("\n")
# print(*set(books) , sep="\n")


#ЗАДАНИЕ 2

lst = [
       [11, 12, 13],
       [21, 22, 23],
       [31, 32, 33]
      ]


class IterColumn:
    def __init__(self, list, column):
        self.list = list
        self.column = column
        self.row = -1
        
    def __iter__(self):
        self.row = -1
        return self
        # return iter(( self.list[x][self.column] for x in range(len(self.list))))

    def __next__(self):
        if self.row == len(self.list)-1:
            raise StopIteration
        self.row += 1
        # self.column += self.column
        return self.list[self.row][self.column]

# it = IterColumn(lst, 1)
# for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
#     print(x)

# print('---')
# it_iter = IterColumn(lst,1)
# print(next(it_iter)) 
# print(next(it_iter)) 
# print(next(it_iter)) 


#ЗАДАНИЕ 3

class Tuple(tuple):
    
    def __add__(self, other):
        # return Tuple(tuple(self) + tuple(other))
        return Tuple((*self, *other))
       
    # def __radd__(self, other):
    #     if self.__class__ is it_iter.__class__:

#
#

t = Tuple([1, 2, 3])
t = t + "Python"

# print(t)
# print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
# t = (t + "Python") + "ООП"
# t2 = t + [4, 5]
# print(*t2,sep='\n')

# print (t) # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n', 'P', 'y', 't', 'h', 'o', 'n', 'О', 'О', 'П')


#ЗАДАНИЕ 4
import re
class CardCheck:

    @classmethod
    def check_card_number(cls, number):
        print(number)
        # print(re.findall(r"\d{4}-\d{4}-\d{4}-\d{4}", number))
        return True if re.match(r"\d{4}-\d{4}-\d{4}-\d{4}", number) is not None else False


    @classmethod
    def check_name(cls, name):
        return True if re.match(r"[A-Z]+ [A-Z]+\b", name) is not None else False

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI SERGEEV")
print(is_number)
print(is_name)