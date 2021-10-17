# -- coding: utf-8 --

def n8(n):
    if n <= 9:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end='')
            print()
n8(int(input('n: ')))
  