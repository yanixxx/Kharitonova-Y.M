# -- coding: utf-8 --

def fib(n, k):
    G1, G2 = 1, 1
    m = [G1, G2]
    for i in range(2, n):
        G1, G2 = G2, G1 + G2
        m.append(G2)
    print(sum(m[k-1:]))  
fib(int(input('Кол-во чисел из ряда: ')), int(input('Номер с которого начать: ')))