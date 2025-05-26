import re

cities = 'Москва Питер Орел Сочи'
cities = cities.split()
cities = map(str.istitle, cities)


# print(all(cities))
#
# cities1 = 'Москва Питер Орел Сочи' # все города с большой буквы
# search1 = re.findall(r'([А-ЯЁ]\w+)', cities1)
# print(search1)
#
# cities = 'Анапа Анадырь Абакан Альметьевск анапа' # все с буквы А
#
# search1 = re.findall(r'А\w+', cities)
# print(search1)

dig = '1 2 22 33 44 55 111'# в строке все числа


# search = re.findall(r'\d+', dig)

# print(len(dig.split()) == len(search))
#
#
# search = map(str.isdigit, dig.split())
#
# print(*search)


# print('В строке есть не числовых значений' if re.search(r'(?i)[^0-9 \n]', dig) else 'В строке все значения числа'))

string = 'ab аб 1 a1 фb2  c3 abc100 10' # в строке нет русских букв

res = map(str.isascii, string.split())


# print(*res)

string = '1,, a1! фb2 c3 abc100 10' # в строке нет знаков препинания

res = map(str.isalnum, string)

print(*res)


file_names = '123.com main.py run.py app.py flask.py' # все файлы с расширением *.py

res = map(lambda file: file.endswith('.py'), file_names.split())


print(*res)


file_names = '123.com main.py run.py app.py flask.py' # все файлы с расширением *.py
# match = r'(?i).py {0,10}'
match = r'\b\w+\.py'
search3 = re.findall(match, file_names)
print(search3)