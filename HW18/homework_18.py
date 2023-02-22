class Bot:

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


class TelegramBot(Bot):

    def __init__(self, name):
        super().__init__(name)
        self.chat_id = None
        self.url = None

    def set_url(self, url=None):
        self.url = url

    def set_chat_id(self, chat_id=None):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f"{self.name} bot says {message} to chat {self.chat_id} using url {self.set_url()}")


some_bot = Bot("Marvin")

some_bot.say_name()

some_bot.send_message("Hello")

telegram_bot = TelegramBot("TG")

telegram_bot.say_name()

telegram_bot.send_message('Hello')

telegram_bot.set_chat_id(1)

telegram_bot.send_message('Hello')


class MyStr(str):
    def __str__(self):
        return super().__str__().upper()


my_str = MyStr("test")
print(my_str)


class User:
    def __init__(self, name):
        self.name = name.lower()

    def __eq__(self, other_name):
        return self.name == other_name.name


first_user = User('OLEKSII')
second_user = User('Oleksii')
print(first_user == second_user)

