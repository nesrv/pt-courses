
x = [0, 0, 0, 'bomb', 0, 0, 0]

res1 = all(x)
res2 = any(x)

# print(res1)
# print(res2)

P = ['x', 'x', '0', 'x', 'x', 'x', '0', 'x', 'x']

# v1 = all(P[0:3])
# v2 = all(P[3:5])
# v3 = all(P[6:9])

v1 = map(lambda x : x =='x', P[0:3])
v2 = map(lambda x : x =='x', P[3:6])
v3 = map(lambda x : x =='x', P[6:9])

print(*v1)
# print(all(v1))
# print(all(v2))
# print(all(v3))
