# Условные операторы
from calendar import month

# тернарный оператор
# if elif else
# паттерн matching

day = 1
month = 1
access = False


match day, month:
    case 1, 1 if access:
        print('понедельник', 'январь')
    case 1, _:
        print('просто понедельник')
    case 7, 2:
        print('воскресенье в феврале')
    case 6 | 7, _:
        print('выходные')
    case _, 3:
        print('это какое-то марта')
    case _,_:
        print('неизвестная инфа')

# CTRL ALT L
