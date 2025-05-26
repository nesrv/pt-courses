class Player:

    def __init__(self, *args):
        self.name, self.old, self.score = args

    def __repr__(self):
        return f'{self.name},{self.score}, {self.old}'

    def __bool__(self):
        return int(self.score) > 0

    def __gt__(self, other): #less then
        return int(self.old) > int(other.old)

    def compare_score(self, other):
        return int(self.score) > int(other.score)


class Sorting:

    def sorting_simple(self):
        ...
    def sorting_by_age_score(self):
        ...

players = '''
Смолов; 34; 16
Дзюба; 35; 30
Жирков; 40; 2
Малафеев; 45; -24
Тарасов; 37; 1
Березуцкий; 41; 0
Акинфеев; 37; -95
'''.strip().splitlines()

players = [Player(*player.split('; ')) for player in players]

print(players)

# players = filter(bool, players)
#
# print(*players)

# players = sorted(players)
# print(*players, sep='\n')

# Как отсортировать игроков по по возрасту?

print(players[0].compare_score(players[1]))

players = sorted(players, key = lambda x: bool)