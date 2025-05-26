# times = '''
# 10 150
# 100 110
# 131 170
# 131 180
# 120 130
# '''.strip().splitlines()

times = open("time_present.txt").readlines()

times = [tuple(map(int, t.split())) for t in times]
times = sorted(times, key=lambda x: x[1])
# как отсортировать по времени окончания

lst = [times[0]]

while times:
    user = times.pop(0)
    if user[0] >= lst[-1][1]:
        lst.append(user)

print(len(lst))