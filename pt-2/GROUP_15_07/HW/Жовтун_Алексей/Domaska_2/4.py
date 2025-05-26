# Объявите класс Person, в объектах которого разрешены только локальные атрибуты с именами (ограничение задается через коллекцию __slots__):
#
# _fio - ФИО сотрудника (строка);
# _old - возраст сотрудника (целое положительное число);
# _job - занимаемая должность (строка).
# Сами объекты должны создаваться командой:
#
# p = Person(fio, old, job) Создайте несколько следующих объектов этого класса с информацией:
#
# Суворов, 52, полководец
# Рахманинов, 50, пианист, композитор
# Иванов, 34, программист и преподаватель
# Пушкин, 32, поэт и писатель

class Person:
    __slots__ = ('fio', 'old', 'job')

    def __init__(self, fio, old, job):
        self.fio = fio
        self.old = old
        self.job = job

    def __lt__(self, other):
        return self.old < other.old

    def __repr__(self):
        return f'{self.fio} : {self.old} {self.job}'


persons = '''
Суворов, 52, полководец
Рахманинов, 50, пианист и композитор
Иванов, 34, программист и преподаватель
Пушкин, 32, поэт и писатель
'''.strip().splitlines()
# print(persons)

# p = [pp.split(', ') for pp in persons]
# print(p)

person = [Person(*person.split(', ')) for person in persons]
# print(person)

print(*sorted(person), sep='\n')
