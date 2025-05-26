#n_card=input('Ввести номер карты: ')
n_card=('4274 9910 0017 1851')
pl_syst= {2 : "Мир",
    3 : "American Express, JCB International, Diners Club",
    30: "Diners Club", 36: "Diners Club", 38 : "Diners Club",
    31: "JCB International", 35 : "JCB International",
    34: "American Express", 37 : "American Express",
    4 : "VISA",
    5 : "MasterCard, Maestro",
    50: "Maestro", 56: "Maestro", 57: "Maestro", 58 : "Maestro",
    51: "MasterCard", 52: "MasterCard", 53: "MasterCard", 54: "MasterCard", 55 : "MasterCard",
    6 : "Maestro, China UnionPay, Открыть для себя",
    60 : "Открыть",
    62 : "China UnionPay",
    63: "Maestro", 67 : "Maestro",
    7 : "УЭК (Универсальная электронная карта)"}


s_keys=pl_syst.keys()
if int(n_card[0:2]) in s_keys:
    p=pl_syst[int(n_card[0:2])]
else: p=pl_syst[int(n_card[0])]

print(n_card, '  ',p )