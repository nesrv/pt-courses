# области видимости переменных
# глобальный и локальный контекст

name = "Иван-1"


def say_hi():
    name = "Иван-2"

    def say_bye():

        nonlocal name
        name = "Иван-3"
        print("Привет,", name)

    say_bye()

    print("Привет,", name)

print(name)

say_hi()

print(name)


# print(globals())