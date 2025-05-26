# Магические методы __len__, __abs__

class WordString:

    def __call__(self, indx):
        return self._string[indx]

    def __len__(self):
        return len(self._string)

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        if value and type(value) == str:
            self._string = value.split()
        else:
            raise ValueError("строка не введена или не строка введена")


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
print(n)
print(words(2))
print(words.string)
words.string = 1, 2, 4
