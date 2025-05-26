class DataBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")

    @classmethod
    def del_connect(cls):
        cls._instance = None


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

print(id(db))
print(id(db2))

DataBase.del_connect()

# DataBase._instance = None
# print(DataBase._instance)
# print(DataBase.__dict__)
db3 = DataBase('root', '1234', 80)

print(id(db3))
