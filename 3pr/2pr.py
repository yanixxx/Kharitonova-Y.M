# -- coding: utf-8 --

def n2(A, B):
    if A < B:
        for i in range(A, B + 1):
            print(i, end=' ')
    else:
        for i in range(A, B - 1, -1):
            print(i, end=' ')
n2(int(input('A: ')), int(input('B: ')))