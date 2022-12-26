text = input("Введіть Ваш текст:\n")
if text.isdigit():
    if int(text) % 2 == 0:
        print("Ви ввели парне число")
    else:
        print("Ви ввели непарне число")
else:
    print("Ви ввели текст. Кількість символів:" + str(len(text)))
