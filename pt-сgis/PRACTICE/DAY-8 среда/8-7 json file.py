from json import dump, dumps, load, loads

x = {
    "name": "Виктор",
    "age": 30,
    "city": "Москва",
    "married": True,
    "children": ("Anna", "Bogdan"),
    "pets": None,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]

}

# with open("users.json", 'w', encoding='utf-8') as f:
#     y = dump(x, f, indent=4, ensure_ascii=False)


with open("users.json", encoding='utf-8') as f:
    z = load(f)
    print(z)
    print(z["cars"][1])

# print(y)
# z = loads(y)
#
# print(type(z))
# print(z["cars"][1]['model'])
