# -*- coding: utf-8 -*-

s = input()
f_w = s[:s.find(' ')]
s_w = s[s.find(' ') + 1:]
print(s_w + ' ' + f_w)