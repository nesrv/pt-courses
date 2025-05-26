# StringDigit


class StringDigit(str):
    def __init__(self, string):
        if string.isdigit():
            self.string = string
        else:
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        if other.isdigit():
            self.string += other
            return StringDigit(self.string)
        raise ValueError


    def __radd__(self, other):
        return self + other

sd = StringDigit("123")
print(sd)
# 123
sd = sd + "456" # StringDigit: 123456
print(sd)
sd = "789" + sd # StringDigit: 789123456
print(sd)
sd = sd + "12f" # ValueError
print(sd)