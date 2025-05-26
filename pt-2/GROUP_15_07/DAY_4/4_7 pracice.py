# lambda + key + lst + str


s = '''
зонт=1000
палатка=10000
спички=22
котелок=543
'''.strip().splitlines()

# s = (row.split('=') for row in s)

s = tuple(map(lambda x: x.split('='), s))

print(*s)

res = filter(lambda x: int(x[1]) > 500, s)

# print(*dict(res).keys())

res = map(lambda x: x[0], res)

print(*res)


# отфильтровать (исключить) все предметы
# с весом менее 500