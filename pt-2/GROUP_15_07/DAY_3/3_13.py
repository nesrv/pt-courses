# __iter__ и __next__
# генераторы и итераторы
class frange:

    def __init__(self, start, stop, step):
        self.start = start - step
        self._iter_start = start - 2 * step
        self.stop = stop
        self.step = step

    def __next__(self):
        if self.start + self.step < self.stop:
            self.start += self.step
            return self.start
        else:
            raise StopIteration

    def __iter__(self):
        self._iter_start += self.step
        return self

fr = frange(1.5, 5, 0.5)

for x in fr:
    print(x)

for y in frange(5, 10, 1.1):
    print(y)



from franges import frange # pip install frange-py
from matplotlib.mlab import frange
from scipy import arange
from numpy import arange
#numpy.arange (start, stop, step)