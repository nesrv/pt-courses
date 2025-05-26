
s = 'Петя Варвара Венера Василиса Василий Федор ваня'

# 1) сформировать кортеж из строки
# 2) отобразите  все имена, которые содержат 'ва'

c = tuple(s.split())

for name in c:
    if 'ва' in  name.lower():
        print(name)


res = [name for name in c if 'ва' in  name.lower()]

print(*res)
