class Record:

    # РЕШЕНИЕ ОТ РОМАНА
    def __init__(self, *args, **kwargs):
        self.__dict__ = kwargs

        self._keys = list(kwargs.keys())
        self._values = [kwargs[self._keys[i]] for i in range(len(self._keys))]

    # def __init__(self, *args, **kwargs):
    #     self.__dict__ = kwargs
    #     self._keys = tuple(kwargs.keys())
    #     self._values = tuple(kwargs.values())

    def __getitem__(self, item):
        return self.__dict__[self._keys[item]]

    def __setitem__(self, key, value):
        setattr(self, self._keys[key], value)

    def __repr__(self):
        # return str(self._values[:len(self._keys)])
        return str(self._values) # РЕШЕНИЕ ОТ РОМАНА

r = Record(pk=1, title='Python-2', author='Серов', job="инженер")

print(r[2])

r[1] = 'Супер курс по ООП'
r[2] = 'Снегирев'
print(r)