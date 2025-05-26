from pickle import dump, load


users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34},
    {"virus": 'lambda x,y: x+y'},
    {1,2,3},
    (1,2,3),
]

# with open('users.dat', 'wb') as f1:
#     dump(users, f1)



f2 = open('users.dat', 'rb')

data = load(f2)

print(data)