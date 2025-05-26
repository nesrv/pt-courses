##  НЕ смог доделать, не работает!

class FileReader:

    def __init__(self, filename):
        self.filename = filename

    def read_txt(self):
        return open(self.filename, encoding="utf-8")

class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):

        self._fio = fio
        self._old = int(old)
        self._job = job

    def __repr__(self):
        return f'{self._fio} {self._old} {self._job}'


def main():
    reader = FileReader('txt.txt')
    content = reader.read_txt()
    # person = Person()


    persons = []
    for pers in content:
        _fio, _old, _job = content.split(", ")
        if person(_fio, _old, _job):
            p = persons.append(Person[pers])
            print(p)

if __name__ == "__main__":
    main()

