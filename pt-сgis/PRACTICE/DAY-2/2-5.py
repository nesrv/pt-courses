# Условные операторы


# тернарный оператор
# if elif else
# паттерн matching

a, b, c = 50, 40, 300
a, b, c = sorted((a, b, c))
print(a, b, c)

if a + b > c and a + c > b and b + c > a:
    print('существует')
    if a == b and b == c:
        print('он равностороний')
    elif a == b or b == c:
        print('он равнобедренный')
    elif c ** 2 == a ** 2 + b ** 2:
        print('он прямоугольный')
    else:
        print('он обычный')

else:
    print('не существует')

# CTRL ALT L
