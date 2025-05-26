# области видимости переменных

name = "Илья"

def say_hi():
    global name
    name = "Иван"  # скрываем значение
    print("Привет,", name)

def say_bye():
    print("Пока,", name)

# say_hi()
# say_bye()

x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)


outer()
print("global:", x)
