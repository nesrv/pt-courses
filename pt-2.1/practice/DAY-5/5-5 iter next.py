# __iter__ и __next__


class frange:

    def __init__(self, start=10.0, stop=0.0, step=0.1):
        self.start = start - 2 * step
        self.stop = stop
        self.step = step

    def __next__(self):
        if self.start == self.stop - self.step:
            raise StopIteration

        self.start += self.step
        return self.start

    def __iter__(self):
        self.start += self.step
        return self


r = frange(1, 5, 0.5)

# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

# print(*r)


for x in frange(1, 10, 0.5):
    print(x)


