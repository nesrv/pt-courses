from datetime import datetime, timedelta

user = 'Егор Тимофеев, 09:10, 16:50'

h1, m1 = map(int, '09:10'.split(':'))
h2, m2 = map(int, '16:50'.split(':'))

t1 = timedelta(hours=h1, minutes=m1)
t2 = timedelta(hours=h2, minutes=m2)

duration = timedelta(hours=4)

duration_user = t2 - t1

print(duration_user > duration)

print(duration_user , duration)
