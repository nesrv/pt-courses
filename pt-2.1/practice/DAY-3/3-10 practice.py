s = '''
pk: 1
title: "Классы и объекты"
author: "Иван Иванов"
views: 14356
review: 12
'''.strip().replace('"','').splitlines()

s = [row.split(':') for row in s]
s = dict(s)

# class BookStore:
#     pk = 1
#     title = "Классы и объекты"
#     author =  "Иванов"
#     views = 14356
#     review = 12

class Bookstore:
    ...
for key, value in s.items():
    if value.strip().isdigit():
        setattr(Bookstore, key, int(value))
    else:
        setattr(Bookstore, key, value.strip())


print(Bookstore.__dict__)

book1 = Bookstore()
book2 = Bookstore()
book1.author = "Петров"

print(book1.__dict__)
print(book2.__dict__)