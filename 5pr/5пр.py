# -*- coding: utf-8 -*-

def n5():
    matr = []
    while True:
        i = 0
        n = input("Введите число - ")
        if n.isdigit() == False:
            print("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ\n")
        if n == "0":
            break
        else:
            matr.append(n)

    print(len(matr))

n5()
