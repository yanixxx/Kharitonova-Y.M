# -*- coding: utf-8 -*-

def s_f():
    N = int(input("N: "))
    k = int(input("k: "))
    past_num = 0
    present_num = 1
    sumn = 0
    for i in range(2, N+1):
        if k <= i:
            sumn += present_num
        time = present_num
        present_num += past_num
        past_num = time
    return sumn

print(s_f())