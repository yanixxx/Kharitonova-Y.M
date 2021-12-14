# -*- coding: utf-8 -*-

def s_f():
    sum=0
    N = int(input('N: '))
    past_num = 0
    present_num = 1
    for i in range(2, N+1):
        sum += present_num
        time = present_num
        present_num += past_num
        past_num = time

    return sum
print(s_f())

