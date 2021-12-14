# -*- coding: utf-8 -*-

def n1():
    while True:
        i = 0
        n = input("Введите число - ")
        if n.isdigit() == False:
            print("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ\n")
        else:
            break
    while i <= int(n):
        print(i * i)
        i+=1

n1()