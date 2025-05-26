from datetime import datetime, timedelta

class FileReader:

    def __init__(self, filename):
        self.filename = filename

    def read_txt(self):
        return open(self.filename, encoding="utf-8")

class DeltaTime:
    HOURS = 4

    @staticmethod
    def _get_time(t):
        h, m = map(int, t.split(':'))
        return timedelta(hours=h, minutes=m)

    @classmethod
    def __call__(cls, *args):
        t1, t2 = args
        return cls._get_time(t2) - cls._get_time(t1) > timedelta(hours=cls.HOURS)

class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, user):
        f = open(self.filename, 'a', encoding='utf-8')
        print(user, file=f)


def main():
    reader = FileReader('crm_log.txt')
    content = reader.read_txt()
    my_delta = DeltaTime()
    my_writer = FileWriter('best_employees.txt')


    for user in content:
        fio, t1, t2 = user.split(", ")
        if my_delta(t1,t2):
            my_writer.write(fio)

if __name__ == "__main__":
    main()