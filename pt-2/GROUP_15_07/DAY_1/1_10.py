class TriangleChecker:

    def __init__(self, *args):
        self.sides = args


    def is_triangle(self):
        if not all((isinstance(x, (int, float)) for x in self.sides)):
            return 'Нужно вводить только числа!'
        if not all(x > 0 for x in self.sides):
            return 'С отрицательными числами ничего не выйдет!'
        temp = sorted(self.sides)
        if temp[0] + temp[1] < temp[2]:
            return 'Жаль, но из этого треугольник не сделать.'

        return 'Ура, можно построить треугольник!'






tr1 = TriangleChecker(2,2,2)
print (tr1.is_triangle())
