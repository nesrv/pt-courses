# Функция как параметр функции

def do(a,b, op):
    return op(a,b)


def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Функция как результат функции

def select_operation(choice):
    if choice == 1:
        return sum
    else:
        return multiply

# op1 = sum
# op2 = multiply
# res = op2(5,5)
# print(res)
# res3 = do(10,10,multiply)
# print(res3)

op1 = select_operation(1)
res = op1(5,5)
print(res)