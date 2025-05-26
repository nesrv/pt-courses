#ЗАДАНИЕ 1
# menu = "Пункт_1 Пункт_2 Пункт_3 Пункт_4 Пункт_5"

# print(menu.split().index('Пункт_5')+1)

# def show_menu(func):
#     def wrapper(*args):
#         list_menu = func(*args)
#         return print(*[(str(list_menu.index(x) + 1) + ". " + x + "\n") for x in list_menu]) # ++ ?
#     return wrapper


# @show_menu
# def get_menu(s):
#     list_menu = s.split()
#     return list_menu


# get_menu(menu)


#ЗАДАНИЕ 2

numbers = "8 11 -5 4 3 10"

def list_sort(func):
    def wrapper(*args, **kwargs):
        list_numbers = func(*args, **kwargs)
        list_numbers = sorted(list_numbers)
        return list_numbers

    return wrapper


@list_sort
def get_list(lst):
    number_list = [int(x) for x in lst.split()]
    # lstNumber = map(int, lstNumber.split()) 
    return number_list

lst = get_list(input())
print(*lst)

#ЗАДАНИЕ 3 ++

from string import ascii_lowercase, ascii_uppercase
from random import sample

chars = ascii_lowercase + ascii_uppercase



def gen_mail(N):
    while True:
        mail = ''.join(sample(chars, N)) + "@mail.ru"
        yield mail


f = gen_mail(8)

print(*[next(f) + "\n" for _ in range(5)])