def decorator(func):
    def wrapper():
        func()
    return wrapper

@decorator
def my_func():
    print("третий лишний")


# d1 = decorator(my_func)

my_func()

