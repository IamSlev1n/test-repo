import time

user_input = input("Введіть Ваш текст або число:\n")
if user_input.isdigit():
    if int(user_input) % 2 == 0:
        print("Це парне число")
    else:
        print("Це непарне число")
elif all(x.isalpha() or x.isspace() for x in user_input):
    upper_text = 0
    lower_text = 0
    spaces = 0
    for sign in user_input:
        if sign.islower():
            lower_text += 1
        elif sign.isupper():
            upper_text += 1
        else:
            spaces += 1
    print(f"У вашому тексті {upper_text} літери у верхньому регістрі, {lower_text} літери у нижньому регістрі та {spaces} пробілів")
else:
    print('Ви ввели символ')

while True:
    print(" I love Python")
    time.sleep(4.2)
