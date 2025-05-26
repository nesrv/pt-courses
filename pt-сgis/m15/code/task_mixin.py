class Digit:
    def __init__(self, value):
        if type (value) == int or type(value) == float:
            self.name = value
        else:
            raise TypeError('значение не соответствует типу объекта')

class Integer(Digit):
    def __init__(self, value):
        if type(value) == int:
            super().__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        if type(value) == float:
            super().__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        if value > 0:
            super().__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        if value < 0:
            super().__init__(value)
        else:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)


x = Integer(4)

digits = [
    PrimeNumber(1), PrimeNumber(2), PrimeNumber(3),
    FloatPositive(2.1), FloatPositive(3.2), FloatPositive(4.3),
    FloatPositive(5.4), FloatPositive(6.5)
    ]


lst_positive = list(filter(lambda x: isinstance(x, Positive),digits))
lst_float = list(filter(lambda x: isinstance(x, Float),digits))
