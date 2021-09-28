# -- coding: utf-8 --
seconds = int(input("Введите количество секунд: "))
print(f"{seconds} секунд это:", seconds // 86400, ':', round(seconds / 3600, 2), ':', round(seconds / 60, 2))