

class Person:
    __slots__ = "_fio", "_old", "_job"


    def __init__(self, *args):
        self._fio, self._old, self._job = args


    def __repr__(self):
        return f'{self._fio}'

text = '''
Суворов, 52, полководец
Рахманинов, 50, пианист и композитор
Иванов, 34, программист и преподаватель
Пушкин, 32, поэт и писатель
'''.strip().splitlines()

print(text)


p1 = Person('Рахманинов', 50, 'пианист')
print(p1.__slots__)

persons = [Person(*row.split(', ')) for row in text]

print(persons)

print(sorted(persons))