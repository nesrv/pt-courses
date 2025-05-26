
class MediaPlayer:

    def open(self,file):
        self.filename = file
    
    def play(self):
        print (f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()


class Soda:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')

 
# Тесты
drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()




class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data
        

    def draw(self):
        for i in self.data:
            if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1]:
                print (i, end=' ')


graph_1 = Graph()
graph_1. set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()





class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'
 
 
# Тесты
triangle1 = TriangleChecker([2, 3, 4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([77, 3, 4])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())



s = '''
Design, develop, maintain and test cloud applications in Python, and document API for cloud services.
design, develop,          and test cloud applications in Python, and document API for       services.
Design,        ,          and      cloud              in Python, and document     for       services.
'''


def data():    
    return s.strip()
    
def first(arg): # Подсчет слов
    return f'Результат первой функции {len(arg.split())}\n'
def two(arg): # Слово и его кол-во
    return f'Результат второй функции {Counter(arg.split())}\n'
def three(arg): # Слово и его кол-во в виде namedtuple
    name = namedtuple('NAME', ['word', 'count']) 
    return f'Результат третьей функции {tuple(name(word, arg.count(word)) for word in set(arg.split()))}'


print(first(data()))
print(two(data()))
print(three(data()))