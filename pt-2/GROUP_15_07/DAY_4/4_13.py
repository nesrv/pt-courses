# Комбинаторика в Python

from itertools import *

# content ='🧀🍄🍖'
#
# pizza = combinations(content,2)
# # коминации (без повторов)
# print(*pizza, sep='\n', end='\n\n')
#
# pizza = permutations(content, 2)
# # перестановки # (сочетания без повторов)
#
# print(*pizza, sep='\n', end='\n\n')
#
# pizza = product(content, repeat=2)
# print(*pizza, sep='\n', end='\n\n')
# # сочетания (все возможные сочетания)
#
# pizza = combinations_with_replacement(content,2)
#
# print(*pizza, sep='\n', end='\n\n')
# сочетаний элементов с повторением
# пересечение двух множеств c исключением

w = 'ТРАТАТА'

print(w)
res = tuple(permutations(w, 7))
print(len(res))

codes = '1234'

comb_codes = product(codes, repeat=5)
# counter = 0

# for code in comb_codes:
#     if code.count('1') == 2:
#         counter +=1

res = (1 for code in comb_codes if code.count('1') == 2)

# print(counter)
print(sum(res))

word = 'ПЯТНИЦА'
comb_words = product(word, repeat=5)

res = (1 for w in comb_words if w[0] != "Н" and w.count('Я') == 1)

print(sum(res))


