class Telegram:
    msglst = list()

    @classmethod
    def add_message(cls, msg):
        cls.msglst.append(msg)
        print(f"+ {msg.text}")

    @classmethod
    def remove_message(cls, msg):
        print(f"- {msg.text}")
        cls.msglst.remove(msg)

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like
        print(f"* {msg.text}")

    @classmethod
    def show_last_message(cls, numb):
        if numb < 0:
            numb = -numb
        if numb == 1:
            print(cls.msglst[-numb:])
        else:
            print(cls.msglst[-numb:-numb+1])

    @classmethod
    def show_messages(cls):
        print(cls.msglst[:])

    @classmethod
    def total_messages(cls):
        return len(cls.msglst)


class Message:

    def __init__(self, text):
        self.text = text
        self.fl_like = False

    def __repr__(self):
        return self.text


msg = Message("01 Hello!!")
Telegram.add_message(msg)

for i in range(1, 5):
    Telegram.add_message(Message(f"{i} msg"))
for i in range(1, 5+1):
    Telegram.show_last_message(i)
print(msg.fl_like)
Telegram.set_like(msg)
print(msg.fl_like)
print(Telegram.total_messages())
Telegram.remove_message(msg)
for i in range(1, 5+1):
    Telegram.show_last_message(i)
print(Telegram.total_messages())
Telegram.show_messages()

