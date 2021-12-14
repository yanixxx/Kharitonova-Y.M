# -*- coding: utf-8 -*-

def n2():
    while True:
        i = 2
        n = input("Введите число - ")
        if n.isdigit() == False or int(n) < 2 :
            print("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ\n")
        else:
            break
    while int(n) % i != 0:
        i += 1
    print(i)
    
n2()
