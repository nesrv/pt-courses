# Замыкания
# глобальный и локальный контекст


# def say_name(name):
#     def say_bye():
#         print("Привет,", name)
#     say_bye()


def say_name(name):
    def say_bye():
        print("Привет,", name)
    return say_bye


f1 = say_name("Иван")
f2 = say_name("Роман")


f1()

f2()



