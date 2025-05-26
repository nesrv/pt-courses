# distance = 10
# day = 1
# x = int(input("Введите расстояние, км: "))
#
# while distance <= x:
#     distance = distance + (distance * 0.1)
#     day = day + 1
#
#
# print("На",day,"- й день лыжник пробежит больше", x, "км", distance)

# 10
# 11
# 12.1
# 13.31

# циклом for ?
distance = 10
x = int(input("Введите расстояние, км: "))

for day in range(1, 10 ** 10):
    distance *= 1.1
    if distance > x:
        break

print("На", day, "- й день лыжник пробежит больше", x, "км", distance)