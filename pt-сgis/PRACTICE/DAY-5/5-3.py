print("Я к вам пишу – чего же боле?")

e = ZeroDivisionError("Деление на ноль")

# raise e


x = 5
y = 10

# assert x > y, 'выполнение запрещено'

def add(a, b):
    return a + b




assert add(2, 2) == 4, 'тест не пройден'
assert add(3, 1.0) == 4, 'тест не пройден'
assert add('3', '3') == '33', 'тест не пройден'
