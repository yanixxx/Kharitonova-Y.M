# -- coding: utf-8 --

def necht(A, B):
    if A > B:
        for i in range(A, B - 1, -1):
            if i % 2 != 0:
                print(i, end=' ')
necht(int(input('A: ')), int(input('B: ')))