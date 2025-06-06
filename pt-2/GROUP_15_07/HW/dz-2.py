class Person:
    __slots__ = "_fio", "_old", "_job"

    def __init__(self, *args):
        self._fio, self._old, self._job = args

    def __repr__(self):
        return f"{self._fio} : {self._old} {self._job}"

    def __lt__(self, other):
        return self._fio < other._fio


text = """Суворов, 52, полководец
Рахманинов, 50, пианист композитор
Иванов, 34, программист и преподаватель
Пушкин, 32, поэт и писатель""".strip().splitlines()



persons = [Person(*row.split(', ')) for row in text]


print(*sorted(persons), sep='\n')

