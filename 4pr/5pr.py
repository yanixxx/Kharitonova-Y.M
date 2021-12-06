# -- coding: utf-8 --

def strk():
	s=str(input('строка: '))
	if s.count('f')==1:
		a=s.find('f')
		return a
	elif s.count('f')>=2:
		b=(s.find('f'),s.rfind('f'))
		return b
	else:
		return 	
print(strk())