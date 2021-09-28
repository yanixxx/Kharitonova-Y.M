# -- coding: utf-8 --
name = input ('имя = ')
age = int (input ('возраст = '))
if 0<age<75 and name != 'Иван':
    if age > 16:
        print ('поздравляем вы поступили в ВГУИТ')
    elif age < 16:

        ost = 16 - age
        print ('сначало нужно окончить школу, тебе осталось учиться:',ost)
else:
    print('не подходите')