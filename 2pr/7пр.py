# -- coding: utf-8 --
def year(D):
    if (D % 4 == 0 or D % 400 == 0) and D % 100 != 0:
        return 'Да'
    else:
        return 'Нет'
print(year(int(input("Введите год: "))))

