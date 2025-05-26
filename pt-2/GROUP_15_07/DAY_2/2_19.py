# _iadd_ +=
# _isub +=
# _imul_ *=
class NewList(list):

    def __sub__(self, other):
        l1 = [(x, type(x)) for x in self]
        l2 = [(x, type(x)) for x in other]
        for x in l1:
            if x in l2:
                l1.remove(x)

        return list([x[0] for x in l1])

    def __isub__(self, other):
        # print("__isub__")
        return self.__sub__(other)

    def __rsub__(self, other):
        return other - self


lst1 = NewList([1, True, 2, -4, 6, 10, 11, 15, False, True, 0])
lst2 = NewList([0, 1, 2, 3, True])

res_1 = lst1 - lst2
print(1, res_1)
lst1 -= lst2
print(2, lst1)
res_2 = lst2 - [0, True]
print(res_2)

res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]