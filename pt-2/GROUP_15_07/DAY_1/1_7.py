# Практикум Методы классов
# 1
class MediaPlayer:

    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()


# media1.open("filemedia1")
# media2.open("filemedia2")

# media1.play()
# media2.play()


# 2
class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        # return (x for x in self.data if self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1])
        return (x for x in self.data if x in range(self.LIMIT_Y[0], self.LIMIT_Y[1] + 1))
        # какой объект возвращает return?


graph1 = Graph()
graph1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])


# res = graph1.draw()
# print(next(res))
# print(next(res))
#
# print(*graph1.draw())

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        data = data.split()
        user = dict(zip(self.FIELDS, data))
        self.lst_data.append(user)

    def select(self, a, b):
        if a == 0:
            a = 1
        return self.lst_data[a - 1: b + 1]

s = '''
1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
'''.strip().splitlines()

db = DataBase()
for user in s:
    db.insert(user)

# print(*db.lst_data, sep='\n')

slice_db = db.select(0, 3)
print(*slice_db, sep='\n')

# FIELDS = ('id', 'name', 'old', 'salary')
# #         ['1', 'Сергей', '35', '120000']
# user1 = s[0].split()
#
# print(dict(zip(FIELDS, user1)))
