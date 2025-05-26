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
    print("Чтение базы данных")


@access
def sent_email():
    print("Отправка данных по сети")


read_db()
sent_email()
