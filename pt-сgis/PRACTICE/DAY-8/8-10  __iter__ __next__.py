# Магические методы __iter__ и __next__



class frange:

    def __init__(self, start, stop, step):
        self.start, self.stop, self.step = start - 2*step, stop, step

    def __next__(self):
        if self.start + self.step < self.stop:
            self.start += self.step
            return self.start
        else:
            raise StopIteration

    def __iter__(self):
        self.start = self.start + self.step
        return self

fr = frange(0.5,4,0.5)
#
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))



for x in frange(1,10,2.5):
    print(x, end=' ')