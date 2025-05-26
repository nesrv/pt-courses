#Александр

#Task1

# text='Edit Save Print Exit'

# def show_menu(func):
#     def wrapper(*args,**kwargs):
#         menu=func(*args,**kwargs)
#         for val in enumerate(menu, 1):
#             print(f'{val[0]}. {val[1]}')
        


#     return wrapper

# @show_menu
# def get_menu(s):    
#     return s.split()


# get_menu(text)



#Task2 ++

# def list_sort(func):
#     def wrapper(*args,**kwargs):
#         lstNumber=func(*args,**kwargs)        
#         # lstNumber = map(int, lstNumber) 
#         # print(*sorted(lstNumber))
#         print(*sorted(lstNumber,key=int)) # !!!
#     return wrapper


# @list_sort
# def get_list(lst):
#     return lst.split()
# lst = get_list(input())


#Task3 +++

from string import ascii_lowercase, ascii_uppercase
from random import sample

chars = ascii_lowercase + ascii_uppercase



def gen_mail(N):
    while True:
        five_mail = (''.join(sample(chars, N)) +'@mail.ru\n' for i in range(5))
        yield five_mail

N =int(input())
f = gen_mail(N)

print(*next(f))


