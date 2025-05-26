name = "Иван"

def say_hi():
    # global name
    name = "Егор"
    def say_goodbye():
        nonlocal name
        name = "Петр"
        print("Don't say me goodbye, " + name + "!")

    say_goodbye()
    print(name)


say_hi()

print(name)