# Декораторы функций

user = "admin"

def access(func):
    def wrapper():
        if user == "admin":
            func()
        else:
            print("доступ запрещен")
    return wrapper



@access
def read_db():
    print("reading data base")


@access
def edit_db():
    print("editing data base")


read_db()
edit_db()