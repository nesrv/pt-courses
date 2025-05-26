
from os import walk, stat


# print(*walk('.'), sep='\n')


# for path, dirs, files in walk('c:/'):
#     # print(dirs, files)
#     for file in files:
#         if file.endswith('.exe'):
#             print(file)
#     # for dir in dirs:
#     #     print(dir)


print(stat("TXT.TXT"))