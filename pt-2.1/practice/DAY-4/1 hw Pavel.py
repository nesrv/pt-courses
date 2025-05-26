#ЗАДАНИЕ 1



# class WordString:

#     def __init__(self, string=''):
#         self.__string = string

#     def __call__(self, indx):
#         return  self.__string.split()[indx]

#     def __len__(self):
#         return len(self.__string.split())

#     @property
#     def string(self):
#         return self.__string

#     @string.setter
#     def string(self, value):
#          self.__string = value



# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")


#ЗАДАНИЕ 2

from math import sqrt
class Point:
    __slots__ = 'x', 'y'
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Точка({self.x}, {self.y})'
    def __gt__(self, other):
        return sqrt(self.x**2 + self.y**2) > sqrt(other.x**2 + other.y**2)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __len__(self):
        return round(sqrt(self.x**2 + self.y**2))
    def __abs__(self):
        self.x = abs(self.x)
        self.y = -abs(self.y)

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

#2
max_point = sorted(points)[-1]
print(max_point)

#3
print(points)
#4
p1 = Point(2, 7)
p2 = Point(2, 7)

print(p1 == p2)
#5
all_points = sorted(points)
print(all_points)
x_points = sorted(points, key = lambda x: x.x)
print(x_points)
#6
print(len(p1))
#7
p3 = Point(-2, 7)
abs(p3)
print(p3) # Точка (2,-7)