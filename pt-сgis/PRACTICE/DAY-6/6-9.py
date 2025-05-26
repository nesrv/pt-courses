# Комбинаторика в Python

from itertools import *

content = "🍕🍖🍄"


pizza1 = combinations(content, 2) # без повторов уник сочетания
print(*pizza1, sep='\n')

print('-' * 20)

pizza2 = permutations(content, 2)

print(*pizza2, sep='\n') #

print('-' * 20)

pizza3 = product(content, repeat=2)

print(*pizza3, sep='\n') #

pizza4 = combinations_with_replacement(content, 2)
print('-' * 20)
print(*pizza4, sep='\n') # сочетаний элементов с повторением


code = '1234'
all_codes = product(code, repeat=5)

cnt = 0
for cod in all_codes:
    if cod.count('1') == 2:
        cnt+=1

print(cnt)

word = 'год'
all_words = product(word, repeat=6)

cnt = 0

for word in all_words:
    if word[0] != 'о':
        cnt+=1

print(cnt)






