# -*- coding: utf-8 -*-

def n7():
    counter = 0
    loopCount = 0
    while True:
        while True:
            x = input("Введите число - ")
            if x.isdigit() == False:
                print("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ\n")
            else:
                break
        x=int(x)
        if x == 0:    
            break           
        if(loopCount != 0):
            if(x > container):
                counter += 1
        container = x
        loopCount+=1
    print(counter)

n7()