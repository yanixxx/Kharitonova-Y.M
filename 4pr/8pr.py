# -- coding: utf-8 --

def str(s):
    print((s[s.find('h') + 1:s.rfind('h'):])[::-1])
str(input('строка: '))