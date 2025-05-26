# Функция как тип
# Функция как параметр функции
# Функция как результат функции


def do(a,b, func):
    return func(a,b)

def sum(a, b): return a + b
def multiply(a, b): return a * b


# print(do(10,5, multiply))


def select_oper(choice):
    return sum if choice == 1 else multiply

# op1 = select_oper(1)
# print(op1(10,20))

# Фабрика функций

dict_func = {
    "plus": sum,
    "mul": multiply,
    "pow" : pow,
    # "divide": lambda x,y : x/y
}

print(dict_func["plus"](10,10))
print(dict_func["pow"](2,10))
print(dict_func["divide"](100,5))

