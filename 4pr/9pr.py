# -- coding: utf-8 --

def str(s, symboldelete):
    s = s.replace(symboldelete, '')
    print(s)
str(input('строка: '), input('удалить символ: '))