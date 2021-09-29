# -- coding: utf-8 --
print("Введите a,b,l,N, переменные <> нулю")
a=int(input())
b=int(input())
l=int(input())
N=int(input())
len=l*2+b*(N-2)+a*(N-1)
print("Длина шнурка должны быть = ",len)
