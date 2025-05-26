


def say_name(name):
    def say_goodbye():
        print("Don't say me goodbye, " + name + "!")
    return say_goodbye



f = say_name("Sergey")
f()

say_name('Павел')()