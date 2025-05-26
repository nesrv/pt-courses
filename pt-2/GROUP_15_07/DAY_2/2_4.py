# класс-функтор

class Counter:

    # def __new__(cls, *args, **kwargs):
    #     ...

    def __init__(self, counter=0):
        self.__counter = counter

    def __call__(self, step=1):
        self.__counter += step
        return self.__counter


c1 = Counter(5)

c2 = Counter(10)

print(c1(), c2(2))
print(c1(), c2(3))
print(c1(), c2(10))
