# -*- coding: utf-8 -*-

def n6():
    matr = []
    while True:
        i = 0
        n = input("Введите число - ")
        if n.isdigit() == False:
            print("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ\n")
            break
        if n == "0":
            break
        else:
            matr.append(int(n))

    print(sum(matr)/len(matr))

n6()
