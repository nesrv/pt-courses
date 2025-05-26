
# Декораторы функций


def decorator(func):
    def wrapper():
        print("--- перед вызовом функции ---")
        func()
        print("--- после вызова функции ---")
    return wrapper

@decorator
def some_func():
    print("Вызов функции some_func")

@decorator
def some_func_2():
    print("Математика")


some_func()
some_func_2()
