import json
import time
import re
from datetime import datetime


def name_time_decorator(func):
    def inner1(*args, **kwargs):
        ret = func(*args)
        file = open("func_log.txt", "a+")
        file.write(f"Function '{func.__name__}' started at {datetime.now()}\n")
        file.close()
        return ret
    return inner1


@name_time_decorator
def read(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)


@name_time_decorator
def write(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)



# contacts = {'mom': '+1111111', 'dad': '+2222222', 'sister': '+3333333', 'brother': '+4444444', 'uncle': '+5555555'}

""" Here are commands which you can use in this app:
stats - shows q-ty of contacts
add - add a new contact (name and phone)
delete - delete contact be name
contacts_list - shows name of all
show_name - shows contact phone number by name
show_all - shows full dict
"""
try:
    file_name = input("Insert a name of contact book:\n")
    contacts = read(file_name)
except FileNotFoundError:
    data = {}
    contacts = write(data, file_name)
    contacts = read(file_name)
while True:
    command = input("\033[37m{}".format("\nWelcome to the phone book!\n\n"
                    "Commands that you can use:\n"
                    "   stats - shows q-ty of contacts\n"
                    "   add - add a new contact\n"
                    "   delete - delete contact that is already in contact book\n"
                    "   contacts_list - shows list of contacts name\n"
                    "   show_name - info about contact\n"
                    "   show_all - whole book listed\n"
                    "Insert your command:\n"))
    if command == 'stats':
        stats = len(contacts)
        print(stats)
    elif command == 'add':
        name_add = input('Insert a name of contact you want to add:\n')
        if name_add not in contacts:
            pattern = '^(\\+380|380|80|0)[0-9]{9}$'
            phone = input('Insert contact\'s phone in format \"+380xxxxxxxxx\" :\n')
            ukr_phones = re.match(pattern, phone)
            if ukr_phones:
                contacts[name_add] = ukr_phones.group()
                write(contacts, file_name)
            else:
                print(f"Invalid format of {phone} phone number. You can use:"
                      "+380********* or "
                      "380********* or "
                      "80********* or "
                      "0*********")
        else:
            print("\033[31m{}".format(f"Sorry, name {name_add} is already in contacts book. Try another name"))
    elif command == 'delete':
        name_del = input('Insert a name of contact you want to delete:\n')
        if name_del not in contacts:
            print("\033[31m{}".format("There is no contact with such name in contact book"))
        else:
            del contacts[name_del]
            write(contacts, file_name)
    elif command == 'contacts_list':
        for contact in contacts:
            print(contact)
    elif command == 'show_name':
        name_info = input('Insert contact name to check info:\n')
        print(contacts.get(name_info))
    elif command == 'show_all':
        print(contacts)
    else:
        print("\033[31m{}".format("Command unknown. Try one more time"))


    class MyCustomException(Exception):
        def __init__(self, message):
            self.message = message
            file_error = open("exception_log.txt", "a+")
            file_error.write(f"Exception with message '{message}' faced at {datetime.now()}\n")
            file_error.close()


    inp = input("Input some integer:")

    try:
        if not inp.isdigit():
            raise MyCustomException("Custom exception is occurred")
    except MyCustomException as exc:
        pass

