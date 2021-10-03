# -- coding: utf-8 --
def year():
    print("Введите год")
    y = int(input())
    if (y % 4 == 0) and (y % 100 > 0) or (y % 400 == 0):
        return 'да'
    else:
        return 'нет'

print (year())
