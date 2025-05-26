# ДЗ 2
class Person:
    __slots__=("_fio","_old","_job")

    def __init__(self, fio, old, job):
        self._fio=fio
        self._old=old
        self._job=job

    def __lt__(self, other):
        return self._fio<other._fio

    def __repr__(self):
        return f" {self._fio}: {self._old} {self._job}"

persons=[Person("Суворов", 52, "полководец"),
Person("Рахманинов", 50, "пианист, композитор"),
Person("Иванов", 34, "программист и преподаватель"),
Person("Пушкин", 32, "поэт и писатель")]

print(*sorted(persons),sep="\n")