# -- coding: utf-8 --

def str(s):
    if s.count('f') == 1:
        print(s.find('f'))
    elif s.count('f') > 1:
        print(s.find('f'), s.rfind('f'))
    else:
        return ''
str(input('строка: '))