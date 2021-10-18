# -- coding: utf-8 --

def str(s):
    s1 = (s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])
    print(s1)
str(input('Строка: '))