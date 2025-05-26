# множество
# неупорядоченная 'изменяемая' коллекция
# уникальных данных


# Длина пароля не менее 5 символов
# Содержит буквы латинского алфавита как в верхнем (2), так и в нижнем регистре
# Хотя бы одну цифру от 0 до 9
# Хотя бы один спец.символ: "@,#,%,&

from string import ascii_uppercase, ascii_lowercase, digits

password = '1Da#CZ'
spec = set('@#%&')


if len(password) >= 5 \
        and (set(password) & set(ascii_lowercase)) \
        and len(set(password) & set(ascii_uppercase)) > 2 \
        and (set(password) & set(digits)) \
        and (set(password) & set(spec)):
    print('ok')

else:
    print ('not ok')
