from datetime import  timedelta
from csv import writer

f = open("crm_log.txt", encoding='utf-8')

def get_time(t):
    h, m = map(int, t.split(':'))
    return timedelta(hours=h, minutes=m)


def get_delta_time(t1,t2):
    t1 = get_time(t1)
    t2 = get_time(t2)
    return t2 -  t1


def write_users_to_file(fio, delta):
    f = open("best_employees.csv", "a", encoding='utf-8', newline='')
    data = [fio, delta]
    w = writer(f)
    w.writerow(data)



for user in f:
    fio, t1, t2 = user.strip().split(', ')
    delta = get_delta_time(t1,t2)
    if get_delta_time(t1,t2) > timedelta(hours=4):
        write_users_to_file(fio, delta)


