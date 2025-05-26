from random import sample, randint


class RandomPassword:

    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars, self.min_length, self.max_length = psw_chars, min_length, max_length

    def __call__(self, *args, **kwargs):
        return ''.join(sample(psw_chars, randint(self.min_length, self.max_length)))


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)
psw = rnd()

print(psw)
print(rnd())
print(rnd())
print(rnd())
