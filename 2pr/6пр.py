# -- coding: utf-8 --
def BW(a, b, c, d):
    if a in range(1, 9) and b in range(1, 9) and c in range(1, 9) and d in range(1, 9):
        if (a+b+c+d) % 2 == 0:
            return 'Да'
        else:
            return 'Нет'
    else:
        return "Введённое число должно быть от 1 до 8"
print(BW(int(input('a: ')), int(input('b: ')), int(input('c: ')), int(input('d: '))))
