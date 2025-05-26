from random import randint, sample


class RandomPassword:

    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length


    def get_rnd(self):
        return randint(self.min_length, self.max_length+1)

    def __call__(self):
        return (''.join(sample(self.psw_chars, self.get_rnd()))
                for _ in range(3))


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length,)

passwords = rnd()
print(*passwords)

print(*rnd())
