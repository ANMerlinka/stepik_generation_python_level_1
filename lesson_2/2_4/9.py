#Разделяй и властвуй
#Напишите программу, которая считывает целое положительное число xx и выводит на экран последовательность чисел x, \, 2x, \, 3x,\,4xx,2x,3x,4x и 5x5x, разделённых тремя черточками.

a = int(input())

x2 = a * 2
x3 = a * 3
x4 = a * 4
x5 = a * 5

print(a, x2, x3, x4, x5, sep = '---')