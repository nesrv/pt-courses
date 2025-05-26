# f = open('first.TXT','r', encoding='utf-8')
# s = open('second.TXT','r', encoding='utf-8')


# while user := f.readline():
#     print(f"Сотрудник ,", user.strip(), 'должность -', s.readline(), sep=" ", end=" ")


#
# for user in f:
#     print(f'{user.strip()}, должность - {s.readline().strip()}')


f = open("TXT.TXT", encoding='utf-8')

cnt_row = 0
lst_text = f.readlines()

print(f'Количество строк в файле {len(lst_text)}')

f.seek(0)
str_text = f.read()

str_text = str_text.replace('.','')
str_text = str_text.split()
str_text = [word for word in str_text if word.isalpha()]


print(f'Количество слов:  {len(str_text)}')


f.seek(0)
str_text = f.read()
str_text = str_text.replace('.','').replace(' ','').replace('\n','')
print(f'Число символов:  {len(str_text)}')

