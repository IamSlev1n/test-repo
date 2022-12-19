import time

user_input = input("Введіть Ваш текст або число:\n")
upper_text = 0
lower_text = 0
spaces = 0
if user_input.isdigit():
    if int(user_input) % 2 == 0:
        print("Це парне число")
    else:
        print("Це непарне число")
elif user_input.replace(' ', '').isalpha():

    list_user_input = list(user_input)
    for sign in list_user_input:
        if sign.islower():
            lower_text += 1
        elif sign.isupper():
            upper_text += 1
        else:
            continue
    print(f"У вашому тексті {upper_text} літери у верхньому регістрі, {lower_text} літери у нижньому регістрі")
else:
    print('Ви ввели символ')

while True:
    print(" I love Python")
    time.sleep(4.2)