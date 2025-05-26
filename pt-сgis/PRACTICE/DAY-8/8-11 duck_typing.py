# Утиная типизация

class Meter:
    def __len__(self):
        return 1_000


print(len([1,2,3]))
print(len("утка"))


m= Meter()
print(len(m))