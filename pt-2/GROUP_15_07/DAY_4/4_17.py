def print_data(user):
    match user:
        case "Олег", 37:
            print("наш человек")

        case "Олег", age:
            print("Олег", age)

        case  name, 22:
            print(name)

        case name, age:
            print(name, age)

        case _:
            print("пока наш человек")


# print_data(("Олег", 37))
# print_data(("Олег", 28))
# print_data(("Сергей", 22))
# print_data(("Боб", 22))
# print_data(("Борис", 41))
# print_data(("Олег", 33, "Google"))



# def print_people(people):
#     match people:
#         case ["Олег", "Сергей", "Борис"]:
#             print("наши люди")
#         case ["Олег", _, _]:
#             print("наши люди-2")
#         case [_,_,_]:
#             print("три объекта в списке")

# def print_people(people):
#     match people:
#         case ["Олег"| "Алиса" ,*_]:
#             print("Олег и наши люди")
#         case [_,_,_]:
#             print("три объекта в списке")


def print_people(people):
    match people:
        case ["Олег"| "Алиса", *_] | ["Олег", "Сергей", "Борис"]:
            print("Олег и наши люди")
        case [_,_,_]:
            print("три объекта в списке")


print_people(["Олег", "Сергей", "Борис"])
print_people(["Олег", "Михаил", "Борис"])
print_people(["Алиса-1", "Вика", "Катя"])
print_people(["Олег", "Катя"])
print_people(["Олег"])



