class Player:
    def __init__(self, name, old, score):
       self.name = name
       self.old = int(old)
       self.score = int(score)

    def __bool__(self):
        return self.score > 0

    def __len__(self):
        return self.score if self.score > 0 else 0

    def __repr__(self):
        return f'{self.name},{self.score}'

    def __lt__(self, other):
        return self.old < other.old

lst_in = '''
Смолов; 34; 16
Дзюба; 35; 30
Жирков; 40; 2
Малафеев; 45; -24
Тарасов; 37; 1
Березуцкий; 41; 0
Акинфеев; 37; -95
'''

players = lst_in.strip().splitlines()

lst_players = [Player(*player.split('; ')) for player in players]

players_filtered = filter(bool, lst_players)
print(*players_filtered)

players_sorted = sorted(lst_players, key=len)
print(players_sorted)

# print(lst_players[0] < lst_players[2])