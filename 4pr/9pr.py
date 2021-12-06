# -- coding: utf-8 --

def strk():
	s=str(input('строка: '))
	z=str(input('символ: '))
	a=(s.replace(z,''))
	return a
print(strk())