# -- coding: utf-8 --

s=str(input("строка: "))
a=s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2]
print(a)