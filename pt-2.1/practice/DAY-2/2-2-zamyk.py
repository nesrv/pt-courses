# Замыкания

def say_name(name):
    def say_goodbye():
        print("Don't say me goodbye, " + name + "!")

    return say_goodbye


f = say_name("Sergey")
f2 = say_name("Илья")


# f()
# f2()


def counter(start=0):
    def step(step=1):
        nonlocal start
        start += step
        return start

    return step


c = counter()
print(c())
print(c())
print(c())
print()

c = counter(10)

print(c(2))
print(c(3))
print(c(5))
