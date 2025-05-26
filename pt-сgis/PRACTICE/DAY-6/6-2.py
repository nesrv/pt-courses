
s = '''
зонт=1000
палатка=10000
спички=22
котелок=543
'''.strip().splitlines()

# s = list(map(lambda row: [row.split('=')[0], int(row.split('=')[1])],s))
sorted_s = []


for row in s:
    thing, value = row.split('=')
    sorted_s.append([thing, int(value)])


res = filter(lambda x: x[-1]>500, sorted_s)

print(*res)


list_of_stop_words = ["в", "и", "по", "за", "на"]

string_to_process = ("Сервис по поиску работы и сотрудников "
                     "HeadHunter опубликовал подборку"
                     " высокооплачиваемых вакансий в России за ноябрь 2024 года"
                     "в Москве. На первых строчках IT-архитекторы и техлиды  ")

res = filter(lambda word : word not in list_of_stop_words, string_to_process.lower().split() )

print(*res)