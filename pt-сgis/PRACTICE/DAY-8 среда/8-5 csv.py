from csv import reader, writer, DictWriter

users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]



with open('users.csv', 'w', newline='', encoding='utf-8') as f:
    column = ["name", "age"]
    wr1 = DictWriter(f, fieldnames=column)
    wr1.writeheader()
    wr1.writerows(users)
    user = {
        "name": "Раиль",
        "age" : 30
    }
    wr1.writerow(user)

# with open('users.csv',  newline='', encoding='utf-8') as f:
#     read = list(reader(f)) # генератор
#     # print(next(read))
#     # print(next(read))
#     # print(next(read))
#     # print(next(read))
#     # print(next(read))
#     #
#     print(read)
#     for user in read:
#         print('*', user)

