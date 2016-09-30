#!/usr/bin/env python3
import random

while True:
    pass_len = input("Введите длину желаемого пароля.\nЭто должно быть число в диапазоне от 6 до 64: ")
    if not pass_len.isnumeric():
        print("Вы ввели не число. Попробуйте снова.")
    elif not 6 <= int(pass_len) <= 64:
        print("Ваше число вне диапазона. Попробуйте снова.")
    else:
        break

while True:
    pass_col = input("Укажите количество требуемых паролей.\nЭто должно быть число в диапазоне от 1 до 20: ")
    if not pass_col.isnumeric():
        print("Вы ввели не число. Попробуйте снова.")
    elif not 1 <= int(pass_col) <= 20:
        print("Ваше число вне диапазона. Попробуйте снова.")
    else:
        break


def pass_generator(count_char):
    simbols = "1472583690qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP"
    char_list = list(simbols)
    passw = []
    for item in range(count_char):
        passw.append(random.choice(char_list))
    return "".join(passw)

for i in range(int(pass_col)):
    print(pass_generator(int(pass_len)))
