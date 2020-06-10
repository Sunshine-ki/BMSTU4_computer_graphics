from interface import *
from constants import *


def int_answer(answer):
    try:
        if answer == "":
            print_error("У вас пустой ввод")
            return FALSE
        if len(answer.split()) != 1:
            print_error("У вас больше одного числа.")
            return FALSE

        a = int(answer)
    except:
        print_error("Некорректный ввод")
        return FALSE

    return a


def get_two_answer(answer):
    try:
        if answer == "":
            print_error("У вас пустое поле!")
            return FALSE, FALSE
        if len(answer.split()) != 2:
            print_error("Некорректный ввод.")
            return FALSE, FALSE
        a, b = map(int, answer.split())
    except:
        print_error("Координаты должны быть целого типа")
        return FALSE, FALSE
    return (a, b)
