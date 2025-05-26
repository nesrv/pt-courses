# Магический метод __bool__
from math import dist

class Player:
    def __init__(self, name, old, score):
       self.name, self.old, self.score = name, int(old), int(score)

    def __bool__(self):
        return  self.score > 0

    def __repr__(self):
        return f'{self.name}:{self.score} очк :{self.old} лет'

    def __abs__(self):
        return self.old >= 40

    # Как отсортировать игроков по по возрасту?
    def __lt__(self, other):
        return self.old < other.old

s='''
Смолов; 34; 16
Дзюба; 35; 30
Жирков; 40; 2
Малафеев; 45; -24
Тарасов; 37; 1
Березуцкий; 41; 0
Акинфеев; 37; -95
'''.strip().splitlines()

players = [Player(*player.split('; ')) for player in s]
print(players)

res1 = filter(bool, players)
print(*res1)

res2 = filter(abs, players)
print(*res2)

print(*sorted(players), sep='\n')