# lambda + key

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person("Tom", 38),
          Person("Kate", 31),
          Person("Bob", 42),
          Person("Alice", 34),
          Person("Sam", 25)]
res = map(lambda user: user.name, people)

# print(*res)

a = [4, 32, -10, 1, 7, 12, 122, 340]

b = sorted(a, key=lambda x: x % 10 == 2)

print(b)
