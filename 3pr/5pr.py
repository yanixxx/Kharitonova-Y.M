# -- coding: utf-8 --

def natur():
	sum=0
	n=int(input('натуральное n: '))
	for i in range(1,n+1):
		sum+=i**3
	return sum
print(natur())    