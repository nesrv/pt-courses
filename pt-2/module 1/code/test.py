# x = 3.5
# print(x.as_integer_ratio())

# y = 15

# print(y.bit_count())
# print(type(y))

# x = bin(y)
# print(x)

# from dataclasses import dataclass, field

# @dataclass
# class Point:
#     x: int
#     y: int
#     length: float = field(init=False)
 

#     def __post_init__(self):   
#         self.length = (self.x ** 2 + self.y ** 2) ** 0.5
    
    
# p1 = Point(1,2)
# print(p1)
# print(p1.__dict__)
# print(p1.length)


from collections import Counter
from collections import namedtuple

s = '''
Design, develop, maintain and test cloud applications in Python, and document API for cloud services.
design, develop,          and test cloud applications in Python, and document API for       services.
Design,        ,          and      cloud              in Python, and document     for       services.
'''


def data():    
    return s.strip()
    
def first(arg): # Подсчет слов
    return f'Результат первой функции {len(arg.split())}\n'
def two(arg): # Слово и его кол-во
    return f'Результат второй функции {Counter(arg.split())}\n'
def three(arg): # Слово и его кол-во в виде namedtuple
    name = namedtuple('NAME', ['word', 'count']) 
    return f'Результат третьей функции {tuple(name(word, arg.count(word)) for word in set(arg.split()))}'


print(first(data()))
print(two(data()))
print(three(data()))