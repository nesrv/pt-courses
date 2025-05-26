# Домовая книга, загс, регистрация граждан

# + бракосочетать граждан
# * создавать детей
# solid

class PairMaker:

    def __init__(self, human1, human2):
        self.human1=human1
        self.human2=human2

class Human:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.status = None

    def __add__(self, other):
        if not isinstance(other, Human) or not isinstance(self, Human):
            print('Объект не человек')
            return
        if self.status == None and other.status == None and self.sex != other.sex:
            self.status = other
            other.status = self
        elif self.status:
            print(f'{self} уже в браке')
        elif self.sex == other.sex:
            print('однополых не сочетаем')
        else:
            print(f'{other} уже в браке')

    def __mul__(self, other):
        if self.status == other:
            return Human("Вася", 'm')
        else:
            print("Они не в браке")

    def __repr__(self):
        return self.name


ivan = Human('Иван', 'm')
anna = Human('Анна', 'w')
petr = Human('Петр', 'm')

# ivan.status = anna

# petr + ivan
anna + '100'
user =  ivan * anna

print(user)


