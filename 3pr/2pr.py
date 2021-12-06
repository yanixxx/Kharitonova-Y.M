# -*- coding: utf-8 -*-

def ABtoBA():
    a = int(input("A: "))
    b = int(input("B: "))
    if a < b:
        for i in range(a, b+1):
            print(i)
    else:
        for i in range(a, b-1, -1):
            print(i)
            
    return "Завершение"
print(ABtoBA())