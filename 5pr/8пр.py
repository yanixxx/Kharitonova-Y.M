# -*- coding: utf-8 -*-

def n8():
    counter = 1
    maxStreak = 0
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
    
            if(x == container):
                counter += 1
            else:
                if(maxStreak < counter):
                    maxStreak = counter
                counter = 1
        container = x
        loopCount+=1
    print(max(maxStreak, counter))

n8()