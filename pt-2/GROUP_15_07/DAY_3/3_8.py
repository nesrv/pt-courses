# Магический метод __new__. Singleton

class DataBase:
    __INST = None

    def __new__(cls, *args, **kwargs):

        if cls.__INST is None:
            cls.__INST = super().__new__(cls)

        return cls.__INST

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

db = DataBase('root', '1234', 80)
print(id(db))
db2 = DataBase('root2', '5678', 40)
print(id(db2))
db3 = DataBase('root3', '5678', 40)
print(id(db3))
print(db3.user)