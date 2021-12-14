# -*- coding: utf-8 -*-

def n4():
    while True:
        x = input("Введите число x - ")
        if x.isdigit() == False:
            print("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ\n")
        else:
            break
        
    while True:
        y = input("Введите число y - ")
        if y.isdigit() == False:
            print("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ\n")
        else:
            break
        
    counter = 1
    x=int(x)
    while x < int(y):
        x *= 1.1
        counter+=1
    print(counter)
    
n4()
