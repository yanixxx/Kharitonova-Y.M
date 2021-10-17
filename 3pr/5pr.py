# -- coding: utf-8 --

def nat(n):
    summ = 0
    for i in range(1, n + 1):
        summ += i**3
    print(summ)
nat(int(input('n: ')))     