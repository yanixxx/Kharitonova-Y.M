# -*- coding: utf-8 -*-

n = int (input("Номер элемента ряда Фибоначчи: " ))
fib1 = 1
fib2 = 1
i = 0
while i < n - 2:
    fibsum = fib1 + fib2
    fib1 = fib2
    fib2 = fibsum
    i = i + 1
print("Значение этого элемента:", fib2)