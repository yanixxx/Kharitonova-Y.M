# -*- coding: utf-8 -*-

def n3():
    while True:
        i = 2
        powContainer = 2
        counter = 1
        n = input("Введите число - ")
        if n.isdigit() == False:
            print("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ\n")
        else:
            break
        
    while powContainer * i < int(n):
        powContainer *= i
        counter+=1
    print(powContainer)  
    print(counter)           

n3()