# t = '''
# 10 150
# 100 110
# 131 170
# 131 180
# 120 130
# '''.strip().splitlines()

f = open("time_present.txt")
t = f.readlines()
t = [list(map(int, row.split())) for row in t]

print(t)

t.sort(key=lambda x: x[1])

users = [t.pop(0)]

while t:
    cur_user = t.pop(0)
    if cur_user[0] >= users[-1][1]:
        users.append(cur_user)

print(len(users))