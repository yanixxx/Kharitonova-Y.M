# -- coding: utf-8 --

def fib(n):
    summ = 0
    G1, G2 = 1, 1
    for i in range(2, n):
        G1, G2 = G2, G1 + G2
    print(f'Сумма {n} элементов:', G2)
fib(int(input('Кол-во чисел из ряда: ')))