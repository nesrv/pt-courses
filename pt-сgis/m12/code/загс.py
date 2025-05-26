# Домовая книга, загс, регистрация граждан

from random import choice

users = ("Миша", 'm'), ("Маша", "w")

class Human:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.status = None
        self.children = []

    def __add__(self, human):
        if self.sex != human.sex and not self.status and not human.status:
            self.status = human
            human.status = self
            print("свадьба состоялась между ", self.status, human.status)
        elif self.status or human.status:
            raise TypeError("полигамия запрещена")
        else:
            raise TypeError("двух мужиков не бракосочетаем")

    def __mul__(self, partner):
        if self.status == partner:
            user = choice(users)
            new_human = Human(*user)
            print("родился", new_human)
            self.children.append(new_human)
            partner.children.append(new_human)
            return new_human
        else:
            print("сначала нужно пожениться")

    def __sub__(self, other):
        if self.status == other:
            self.status = other.status = None

    def __repr__(self):
        return f'{self.name} '


ivan = Human('Иван', 'm')
anna = Human('Анна', 'w')
bob = Human('Bob', 'm')
irina = Human('Ирина', 'w')

ivan + anna
baby = ivan * anna
ivan - anna
print(ivan.status)
print(anna.status)
print(1, baby)
ivan + anna
baby = ivan * anna
print(2, baby)
print(anna.children)
print(ivan.children)
