#Task 1
# class WordString:

#     def __init__(self, string=''):
#         self._string=string

#     def __call__(self, indx):
#         words=self._string.split()
#         return words[indx] if 0 <= indx < len(words) else None # !

#     def __len__(self):
#         return len(self._string.split())

#     @property
#     def string(self):
#         return self._string

#     @string.setter
#     def string(self, value):
#         self._string = value

# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(words(2))
# print(f"Число слов: {n}; первое слово: {first}")


# Task 2, 3

from math import hypot
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'точка ({self.x},{self.y})'

    def __gt__(self, other):  # less then
        return hypot(self.x, self.y) > hypot(other.x, other.y)
        
        # return float((self.x**2+self.y**2)**0.5) > float((other.x**2+other.y**2)**0.5)

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]


print(max(points))
print(points)

# Task 4

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'точка ({self.x},{self.y})'

    def __eq__(self, other):  # less then
        return int(self.x) == int(other.x) and int(self.y)==int(other.y) #?


p1 = Point(2, 7)
p2 = Point(2, 7)

print(p1 == p2)

# Task 5



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'точка ({self.x},{self.y})'

    def __gt__(self, other):  # less then
        return float((self.x**2+self.y**2)**0.5) > float((other.x**2+other.y**2)**0.5)

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]


points=sorted(points,reverse=True) # Сортировка по удаленности от начала координат от наибольшего к меньшему
print(points)

from math import dist

# Найти длину ломаной линии Points

d = dist((points[0].x, points[0].y), (points[1].x, points[1].y))
print(d)


d2 = dist((0,0), (3,4))
d3 = dist((0,0,0), (3,4,0))

print(d2)
print(d3)


