# -- coding: utf-8 --

def gg(A, B):
    if A <= B:
        for i in range(A, B + 1):
            print(i, end=' ')
gg(int(input('A: ')), int(input('B: ')))