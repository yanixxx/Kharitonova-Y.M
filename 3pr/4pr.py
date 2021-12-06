# -*- coding: utf-8 -*-

def sumn():
    sumn = 0

    for i in range(int(input("количество чисел: "))):
        sumn += int(input(f"Введите число: "))
    return "Сумма = " + str(sumn)

print(sumn())