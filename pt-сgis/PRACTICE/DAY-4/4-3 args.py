
def f (a,b, *args, c="привет", **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


# f(1,2, 10, 20, число='пи', c="hello", p="привет")


f('a1', "a2", "b3", 'b4', ['b5', 'b6'], c1='1', c2='2', c3=(1, 2, 3), c4=[5, 6, 7])




