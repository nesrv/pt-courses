class Soda:

    @staticmethod
    def get_ingridient(ingridient):
        return ingridient if isinstance(ingridient, str) else None

    # def get_ingridient(self, ingridient):
    #     return ingridient if isinstance(ingridient, str) else None

    def __init__(self, ingridient=None):
        self.ingridient = self.get_ingridient(ingridient)

    def show_my_drink(self):
        print(f'Газировка и {self.ingridient}' if self.ingridient else "Обычная газировка")


soda1 = Soda()
soda2 = Soda("малина")
drink3 = Soda(5)
drink4 = Soda((1,2,32, "привет"))

soda1.show_my_drink()
soda2.show_my_drink()
drink3.show_my_drink()  # Как сделать,
drink4.show_my_drink()  # Как сделать,
# чтобы конструктор работал только со строкой
