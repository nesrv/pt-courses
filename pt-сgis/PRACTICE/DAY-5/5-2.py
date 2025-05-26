from time import ctime

a = 5

print("Я к вам пишу – чего же боле?")
# print(a)

f = open('error-log.txt', 'a', encoding='utf-8')

try:
    print('b')
    # file = open("myfile2.txt")
    10 / a

except Exception as Error:
    print(f"ошибка {Error} в {ctime()}", file=f)

else:
    print('Ошибок не произошло')
finally:
    print("Блок finally выполняется всегда")

