# -- coding: utf-8 --

def chis(N):
    summ = 0
    k = 1
    for i in range(N):
        summ += int(input(f'Число {k}: '))
        k += 1
    print('Сумма: ', summ)
chis(int(input('Кол-во чисел: ')))