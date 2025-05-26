# бинарная сериализация ?
# pickle

import pickle

user = "Tom", 19, {1,2,3}, {1:"один"}


# f = open("user.dat", "wb")
# pickle.dump(user, f)


f = open("user.dat", "rb")
res = pickle.load(f)

print(res)


