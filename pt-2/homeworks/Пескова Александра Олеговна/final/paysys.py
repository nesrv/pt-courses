paymentsystems = {
    'Работает': {
        '2': 'Мир',
        '30': 'DinersClub',
        '36': 'DinersClub',
        '38': 'DinersClub',
        '4': 'VISA',
        '51': 'MasterCard',
        '52': 'MasterCard',
        '53': 'MasterCard',
        '54': 'MasterCard',
        '55': 'MasterCard',
        '62': 'China UnionPay',
        '7': 'УЭК'
    },
    'Не работает':{
        '31': 'JCB Interntional',
        '35': 'JCB Interntional',
        '34': 'American Express',
        '37': 'American Express',
        '50': 'Maestro',
        '56': 'Maestro',
        '57': 'Maestro',
        '58': 'Maestro',
        '60': 'Discover',
        '63': 'Maestro',
        '67': 'Maestro',
    }
}
somecard = '2200300514986874'
def payable(somecard):
    return True if somecard[0] in paymentsystems['Работает'] or somecard[0:2] in paymentsystems['Работает'] else False

print(payable(somecard))