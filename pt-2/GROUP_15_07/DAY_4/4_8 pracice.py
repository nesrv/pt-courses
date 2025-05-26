# lambda + key + lst + str

ranks = '''
рядовойсержантстаршинапрапорщиклейтенанткапитанмайорподполковникполковник
'''


lst_in='''
Жуков=полковник
Иванов=лейтенант
Петров=прапорщик
Сидоров=капитан
Егоров=лейтенант
Смирнов=рядовой
Смирнов2=рядовой
'''.strip().splitlines()

lst= map(lambda row: row.split('='), lst_in)

# print(*lst)

res = sorted(lst, key=lambda user: ranks.index(user[1]))

print(*res, sep='\n')