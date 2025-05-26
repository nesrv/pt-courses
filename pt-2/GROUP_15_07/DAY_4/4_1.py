# Функция как тип
# Функция как параметр функции

def say_hello(): print("Hello")
message = say_hello
message()

def do(a,b, func):
    return func(a,b)

def sum(a, b): return a + b
def multiply(a, b): return a * b

oper = sum

print(oper(5,5))

print(do(10,5, multiply))

