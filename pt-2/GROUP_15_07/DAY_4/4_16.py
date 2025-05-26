# Конструкция match
def f1(n):
    return 1 if n == 1 or n == 0 else f1(n - 1) * n


def f2(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return f2(n - 1) * n


# print(f1(5))
# print(f2(5))

def print_hello(language):
    match language:
        case "russian" | "belorussian":
            print("Привет")
        case "american english" | "british english":
            print("Hello")

        case _:
            print("гудбай")


#
# print_hello("belorussian")
# print_hello("american english")
# print_hello("british english")

color = 0, 0, 10, 2

match color:
    case 1, 1, 1:
        print("белый")
    case 1, 0, 0:
        print("красный")
    case 0, 0, 1:
        print("синий")

    case r, g, b:
        print('пришел', r, g, b)
    case _:
        raise ValueError("Неизвестный цвет")

