# -*- coding: utf-8 -*-

def n2():
    i = 2
    N = int(input("Введите число - "))
    while N % i != 0:
        i += 1
    print(i)
n2()