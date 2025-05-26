
class Card:
    def __new__(cls, number, *args, **kwargs):
        instrance = super().__new__(cls)
        cn = number[::-1]
        tmp1 = 0
        for i in range(1, len(cn), 2):
            num = int(cn[i]) * 2
            if num > 9:
                num = int(str(num)[0]) + int(str(num)[1])
            tmp1 += int(num)
        tmp2 = 0
        for i in range(0, len(cn), 2):
            tmp2 += int(cn[i])
            if ((tmp1 + tmp2) % 10 == 0):
                return instrance

    def __init__(self, *args, **kwargs):
        self._number, self._owner = args

    def __str__(self):
        return f"{self._number}"


card1 = Card('4274991000171851', 'Inna Berezova')
print(card1)
print(card1.__dict__)

card2 = Card('4274990000171851', 'Noname owner')
print(card2)

