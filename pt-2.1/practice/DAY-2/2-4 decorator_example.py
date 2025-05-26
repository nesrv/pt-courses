# Декораторы функций

user = 'admin'
superuser = 'superadmin123'

def super_access(func):
    def wrapper():
        if superuser == 'superadmin':
            return func()
        else:
            print("нет доступа")
    return wrapper

def access(func):
    def wrapper():
        if user == 'admin':
            return func()
        else:
            print("нет доступа")
    return wrapper

@super_access
@access
def read_db():
    print("reading data base")

@access
def change_db():
    print("change data base")

@access
def clean_vacuum_db():
    print("vacuum data base")


read_db()
change_db()
clean_vacuum_db()