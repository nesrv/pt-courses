# Комбинаторика в Python

from itertools import *

content ='🧀🍄🍖'

pizza = combinations(content,2)
# коминации (без повторов)
print(*pizza, sep='\n', end='\n\n')

pizza = permutations(content, 2)
# перестановки # (сочетания без повторов)

print(*pizza, sep='\n', end='\n\n')

pizza = product(content, repeat=2)
print(*pizza, sep='\n', end='\n\n')
# сочетания (все возможные сочетания)

pizza = combinations_with_replacement(content,2)

print(*pizza, sep='\n', end='\n\n')
# сочетаний элементов с повторением
# пересечение двух множеств c исключением

from math import perm, comb

content ='🧀🍄🍖'

count_pizza = comb(3,2)
print(count_pizza)

count_pizza = perm(3,2)
print(count_pizza)