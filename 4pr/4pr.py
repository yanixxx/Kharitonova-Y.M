# -- coding: utf-8 --

def str(s):
    print(s[s.find(' ') + 1:], s[:s.find(' ')])
str(input('Строка: '))