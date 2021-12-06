# -*- coding: utf-8 -*-

A = int(input("A: "))
B = int(input("B: "))
for i in range(A - A % 2 -1, B -1, -2):
    print(i)