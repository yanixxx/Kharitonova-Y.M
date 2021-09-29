# -- coding: utf-8 --
def minl(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
print(minl(int(input('a: ')), int(input('b: ')), int(input('c: '))))
