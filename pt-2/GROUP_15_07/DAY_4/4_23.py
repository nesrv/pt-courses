# Замыкания
# глобальный и локальный контекст

# def counter(start=0):
#     def step(n=1):
#         nonlocal start
#         start += n
#         return start
#     return step
#
# c1 = counter()
# c2 = counter(10)
#
# print(c1(1), c2())
# print(c1(10), c2())
# print(c1(100), c2())

def my_strip(chars=" "):
    def do_strip(string):
        return string.strip(chars)
    return do_strip


strip1 = my_strip()
strip2 = my_strip(" .!,?")

s = "    ... Python .. !!    "
res1 = strip1(s)
res2 = strip2(s)

print(res1)

print(res2)