
class int(int):

    def __add__(self, other):
        return self * other


x = int(10)
x = x + 20


print(x)


# можно ли + сделать умножение чисел