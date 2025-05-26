# Функции высшего порядка

# map lambda  filter reduce

grades = '3 3 5 5 3 3'

# print("отчислен" if '2' in grades else "")

grades = grades.split()

grades = map(int, grades)
grades = map(lambda x: x > 2, grades)

# print("отчислен" if not all(grades) else "учится")


s = [10, 100, 81, 79, 49, 121, 169]


res = filter(lambda x: x ** 0.5 % 1 == 0 , s)

print(*res)

# print((100 ** 0.5) % 1 == 0)
# print((82 ** 0.5) % 1 == 0)

