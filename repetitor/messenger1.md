
## 📄 Техническое задание

###  Простой мессенджер на Python

---

### 🎯 Цель проекта:

Разработать консольное приложение «Простой мессенджер» с использованием объектно-ориентированного программирования. 
Пользователи должны иметь возможность обмениваться сообщениями в формате "один на один", просматривать историю переписки, а также управлять своими чатами.

---

## 📌 Обязательная функциональность (базовый уровень)

### 1. Пользователи

* Класс: `User`
* Поля:

  * `username` — имя пользователя (строка)
  * `inbox` — список полученных сообщений
* Методы:

  * `send_message(to_user, text, chat)` — отправить сообщение
  * `__str__()` — вывод имени пользователя

---

### 2. Сообщения

* Класс: `Message`
* Поля:

  * `sender` — объект `User`, отправитель
  * `receiver` — объект `User`, получатель
  * `text` — текст сообщения (строка)
  * `timestamp` — время отправки (`datetime`)
  * `read` — статус прочтения (`True/False`)
* Методы:

  * `mark_as_read()` — пометить сообщение как прочитанное
  * `__str__()` — форматированный вывод (с временем и отправителем)

---

### 3. Чаты

* Класс: `Chat`
* Поля:

  * `participants` — множество из двух пользователей
  * `messages` — список объектов `Message`
* Методы:

  * `add_message(message)` — добавить сообщение в чат
  * `get_history()` — вывести все сообщения
  * `get_unread_messages(user)` — получить непрочитанные сообщения для пользователя

---

### 4. Мессенджер (система)

* Класс: `Messenger`
* Поля:

  * `users` — список всех зарегистрированных пользователей
  * `chats` — список всех чатов
* Методы:

  * `register_user(username)` — создать нового пользователя
  * `create_chat(user1, user2)` — создать чат между двумя пользователями
  * `get_user(username)` — получить объект пользователя по имени
  * `get_chat(user1, user2)` — найти или создать чат между двумя пользователями

---



```PY
from datetime import datetime

# ----------------------------
# Класс пользователя
# ----------------------------
class User:
    def __init__(self, username):
        self.username = username  # Имя пользователя
        self.inbox = []           # Входящие сообщения (необязательно, но может использоваться)

    def send_message(self, to_user, text, chat):
        # Метод отправки сообщения в указанный чат
        message = Message(sender=self, receiver=to_user, text=text)
        chat.add_message(message)

    def __str__(self):
        return self.username


# ----------------------------
# Класс одного сообщения
# ----------------------------
class Message:
    def __init__(self, sender, receiver, text):
        self.sender = sender              # Объект User, отправитель
        self.receiver = receiver          # Объект User, получатель
        self.text = text                  # Текст сообщения
        self.timestamp = datetime.now()   # Время отправки
        self.read = False                 # Статус прочтения: False по умолчанию

    def mark_as_read(self):
        self.read = True  # Отметить сообщение как прочитанное

    def __str__(self):
        # Строковое представление сообщения
        status = "✓✓" if self.read else "✓"
        time = self.timestamp.strftime("%H:%M")
        return f"[{time}] {self.sender.username} ➜ {self.receiver.username}: {self.text} {status}"


# ----------------------------
# Класс чата между двумя пользователями
# ----------------------------
class Chat:
    def __init__(self, user1, user2):
        self.participants = {user1, user2}  # Уникальное множество из 2 пользователей
        self.messages = []                 # Список всех сообщений в чате

    def add_message(self, message):
        self.messages.append(message)      # Добавляем сообщение в чат

    def get_history(self):
        # Показать все сообщения в чате
        for message in self.messages:
            print(message)

    def get_unread_messages(self, user):
        # Получить список непрочитанных сообщений для конкретного пользователя
        return [msg for msg in self.messages if msg.receiver == user and not msg.read]


# ----------------------------
# Класс системы-мессенджера
# ----------------------------
class Messenger:
    def __init__(self):
        self.users = []  # Все зарегистрированные пользователи
        self.chats = []  # Все активные чаты

    def register_user(self, username):
        # Зарегистрировать нового пользователя
        user = User(username)
        self.users.append(user)
        return user

    def get_user(self, username):
        # Найти пользователя по имени
        for user in self.users:
            if user.username == username:
                return user
        return None

    def create_chat(self, user1, user2):
        # Создать чат между двумя пользователями, если он ещё не существует
        existing = self.get_chat(user1, user2)
        if existing:
            return existing
        chat = Chat(user1, user2)
        self.chats.append(chat)
        return chat

    def get_chat(self, user1, user2):
        # Найти чат между двумя пользователями, если он есть
        for chat in self.chats:
            if {user1, user2} == chat.participants:
                return chat
        return None


# ----------------------------
# Пример использования (демонстрация)
# ----------------------------

# Создаём мессенджер
app = Messenger()

# Регистрируем двух пользователей
alice = app.register_user("Alice")
bob = app.register_user("Bob")

# Создаём чат между ними
chat = app.create_chat(alice, bob)

# Alice отправляет сообщение Bob'у
alice.send_message(to_user=bob, text="Привет, Боб!", chat=chat)

# Bob отправляет ответ
bob.send_message(to_user=alice, text="Привет, Алиса! Как дела?", chat=chat)

# Показываем историю переписки
print("\n📜 История чата:")
chat.get_history()

# Получаем непрочитанные сообщения для Alice
unread = chat.get_unread_messages(alice)
print(f"\n📬 У {alice.username} непрочитанных сообщений: {len(unread)}")

# Отмечаем сообщения как прочитанные
for msg in unread:
    msg.mark_as_read()

# Повторно показываем историю — теперь все сообщения прочитаны
print("\n✅ История после прочтения:")
chat.get_history()


```