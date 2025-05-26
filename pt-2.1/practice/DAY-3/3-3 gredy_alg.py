# s = '''
# 43
# 40
# 32
# 40
# 30
# '''.split()

f = open('boxes.txt')
s = f.readlines()

s = map(int, s)
s = sorted(s, reverse=1)


sklad = [s.pop(0)]

while s:
    cur_box = s.pop(0)
    if sklad[-1] - cur_box >= 3:
        sklad.append(cur_box)


print(len(sklad), sklad[-1])
