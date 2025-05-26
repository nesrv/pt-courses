
from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(card_number):
        for i in card_number.split('-'):
            if not (i.isdigit() and len(i) == 4):
                return False
        return True

    @staticmethod
    def check_name(card_holder):
        for i in card_holder.split(' '):
            for j in i:
                if j not in CardCheck.CHARS_FOR_NAME:
                    return False
        return True


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
print(is_number)
is_name = CardCheck.check_name("SERGEI SERGEEV")
print(is_name)
is_number = CardCheck.check_card_number("123D-5678-9012-0000")
print(is_number)
is_name = CardCheck.check_name("SERGEI SER%GEEV")
print(is_name)
