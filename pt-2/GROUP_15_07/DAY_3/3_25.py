class Validator:

    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):

    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def _is_valid(self, data):
         return self.min_val <= data <= self.max_val and type(data) == float

    def __call__(self, *args, **kwargs):
        return self._is_valid(args[0])


float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])

print(res_1)
print(res_2)
print(res_3)