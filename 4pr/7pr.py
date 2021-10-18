
# -- coding: utf-8 --

def str(s):
    print(s.replace(s[s.find('h'):s.rfind('h') + 1], ''))
str(input('строка: '))