# метод format и f-строки
from itertools import count

name = 'Егор'
first_name = 'Петров'

s = 'Имя: {first_name} Фамилия: {name}'.format(name=name, first_name=first_name)

print(1, s)

# f-строки

s = f'Имя: {name + " Васильевич"} Фамилия: {first_name.upper()}'
print(2, s)
print(f'{32:b}')
print(f'{15:X}')

n = 1/3
r = f'{n:.3%}'
# r = r.zfill(20)
# r = r.ljust(20, '#')
r = r.rjust(20, '+')
print(r)
count_plus = r.count('+')
print(count_plus)
print('33.333' in r)
print('33333' in r)
print('3' in r)
print(r.index('3'))
print(r.rindex('3'))
print(r.startswith('++'))
print("123.pyc".endswith('.py'))
print("123".isdigit())
print("1.23".isdigit())
print("abcЯ".isalpha())
print("ab,cЯ".isalnum())

print('-'* 30)
s = '''
Вася
Петя
Егор
'''.strip().splitlines()

print(s)


