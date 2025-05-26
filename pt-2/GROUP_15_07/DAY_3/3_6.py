class Dimensions:

    @staticmethod
    def _check_abc(*args):
        if not all(x > 0 for x in args):
            raise ValueError("габаритные размеры дб полож числами")

    def __init__(self, *args):
        self._check_abc(*args)
        self.a, self.b, self.c = args

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __lt__(self, other):
        return self.__hash__() < other.__hash__()

    def __len__(self):
        return int(self.a * self.b * self.c)

    def __repr__(self):
        return f'{(self.__hash__())} - {len(self)}'

s = '1 2 3; 4 5 6.78; 1 2 3; 1 1 2.5'
s = s.split('; ')

s = [Dimensions(*map(float,row.split())) for row in s]

# s.sort(key=hash)

print(sorted(s))

s.sort(key=len)

print(s)

