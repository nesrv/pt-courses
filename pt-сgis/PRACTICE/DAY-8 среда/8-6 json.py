from json import dump, dumps, load, loads

x = {
    "name": "Viktor",
    "age": 30,
    "city": "Minsk",
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

y = dumps(x, indent=4)
print(y)
z = loads(y)

print(type(z))
print(z["cars"][1]['model'])
