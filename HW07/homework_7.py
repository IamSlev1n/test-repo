contacts = {'mom': '+1111111', 'dad': '+2222222', 'sister': '+3333333', 'brother': '+4444444', 'uncle': '+5555555'}
""" Here are commands which you can use in this app:
stats - shows q-ty of contacts
add - add a new contact (name and phone)
delete - delete contact be name
contacts_list - shows name of all
show_name - shows contact phone number by name
show_all - shows full dict
"""
while True:
    command = input("\033[37m{}".format("\nВітаємо в телефонній книзi!\n\n"
                    "Команди які можна використовувати:\n"
                    "   stats - показує кількість контактів\n"
                    "   add - дозволяє додати новий контакт\n"
                    "   delete - дозволяє видалити існуючий контакт\n"
                    "   contacts_list - показує список імен контактів\n"
                    "   show_name - показує інформацію про контакт\n"
                    "   show_all - показує весь список контактів з телефонами\n"
                    "Введіть вашу команду:\n"))
    if command == 'stats':
        stats = len(contacts)
        print(stats)
    elif command == 'add':
        name_add = input('Введіть ім\'я контакту, який хочете додати:\n')
        if name_add not in contacts:
            phone = input('Введіть номер телефону контакту, який хочете додати, у форматі \"+xxxxxxx\" :\n')
            contacts[name_add] = phone
        else:
            print("\033[31m{}".format(f"Вибачте, ім\'я {name_add} вже є у телефонній книзі. Спробуйте інше ім\'я."))
    elif command == 'delete':
        name_del = input('Введіть ім\'я контакту, який хочете видалити:\n')
        if name_del not in contacts:
            print("\033[31m{}".format("У телефонній книзі немає контакту з таким ім\'ям"))
        else:
            del contacts[name_del]
    elif command == 'contacts_list':
        for contact in contacts:
            print(contact)
    elif command == 'show_name':
        name_info = input('Введіть ім\'я контакту, номер телефону якого хочете переглянути:\n')
        print(contacts.get(name_info))
    elif command == 'show_all':
        print(contacts)
    else:
        print("\033[31m{}".format("Команда не розпізнана, спробуйте ще раз, будь-ласка."))
