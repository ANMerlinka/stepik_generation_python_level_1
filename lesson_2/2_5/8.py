#Перестановка цифр
#Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.
n = int(input())

a = n // 100
b = (n % 100) // 10
c = n % 10

print(a,b,c, sep='')
print(a,c,b, sep='')
print(b,a,c, sep='')
print(b,c,a, sep='')
print(c,a,b, sep='')
print(c,b,a, sep='')