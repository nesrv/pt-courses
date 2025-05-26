# Циклы
import time

x = 5

while x > -2:
    print('работаю ...', x)
    time.sleep(1)
    x = x - 1
    if x == 0:
        continue
    if x == 0:
        break
else:
    print('happy end')


print("конец цикла")

