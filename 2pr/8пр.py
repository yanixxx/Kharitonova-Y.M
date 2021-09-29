# -- coding: utf-8 --
def same(a, b, c):
    if a == b and a == c:
        return '3'
    elif a == b or a == c:
        return '2'
    else:
        return '0'
print(same(int(input('a: ')), int(input('b: ')), int(input('c: '))))
