import time

user_input = input("Введіть Ваш текст або число:\n")

for sign in user_input:
    if sign.isdigit():
        if int(sign) % 2 == 0:
            print(sign + " - це парне число")
        else:
            print(sign + " - це непарне число")
    elif sign:
        if sign.islower():
            print(sign + " - це літера у нижньому регістрі")
        elif sign.isupper():
            print(sign + " - це літера у верхньому регістрі")
        elif sign.isspace():
            print(sign + " - це символ 'space'")
        else:
            print(sign + " - це символ")

while True:
    print(" I love Python")
    time.sleep(4.2)
