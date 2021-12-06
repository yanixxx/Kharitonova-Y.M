# -*- coding: utf-8 -*-

print ("Введите числа по условию A ≤ B")

A = int (input ('A: '))
B = int (input ("B: "))
if A <= B:
	for i in range(A, B+1):
		print(i)
else:
	print("Другие числа по условию A ≤ B")