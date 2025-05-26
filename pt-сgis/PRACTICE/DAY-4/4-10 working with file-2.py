f = open('TXT.TXT', encoding='utf-8')

# for x in range(10):
#     f.write(str(x ** 2 + 2 * x))
#     f.write('\n')

# print(*f)
# # считать и получить список из чисел

# res = f.read()
# res = res.split()

print(f.readline())
print(f.readline())
print(f.readline())

res = f.readlines()

res = [int(x) for x in res]

print(res)
print(sum(res))

