players = '''
Смолов; 34; 30
Дзюба; 35; 30
Жирков; 40; 2
Малафеев; 45; -24
Тарасов; 37; 1
Березуцкий; 41; 0
Акинфеев; 37; -95
'''.strip().splitlines()

players = [player.split('; ') for player in players]

players = [ [row[0], int(row[1]), int(row[2])] for row in players ]

players.sort(key=lambda x: (x[-1], x[-2]))

print(players)
