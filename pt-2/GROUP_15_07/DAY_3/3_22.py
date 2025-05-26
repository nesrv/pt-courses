class Singleton:
    _GAME = None

    def __new__(cls, *args, **kwargs):
        if cls._GAME is None:
            cls._GAME = object.__new__(cls)

        return cls._GAME


class Game(Singleton):
    def __init__(self, name):
        print(self.__dict__)
        if 'name' not in self.__dict__:
            self.name = name


g1 = Game("ГТА-4")
g2 = Game("тетрис")
print(g2.name)




