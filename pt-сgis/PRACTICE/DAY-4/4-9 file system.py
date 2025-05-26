import os
from os import  name, getcwd, \
    rename, path, remove, listdir, chdir, replace

print(name) # nt
print(getcwd())

# dirs = 'virus/'*10
# makedirs(dirs)

# removedirs(dirs )
# rmdir('HELLO')
# mkdir('HELLO')

# open("TXT.TXT", 'a') # a - append
# if path.exists('TXT.TXT'):
#     rename('TXT.TXT', 'text.txt')


# remove('text.txt')
# chdir('c:/')
# print(*listdir('c:/'), sep='\n')
# print(*listdir(), sep='\n')

files = listdir()

for file in files:
    if 'args' in file:
        print(file)

replace("text.txt", "c:/w25/t.txt")

