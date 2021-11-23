# -*- coding: utf-8 -*-

def n8():
    counter = 1
    maxStreak = 0
    loopCount = 0
    while True:
        x = int(input("Введите число - "))
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