# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input("Введите натуральное число: "))
i = 2 
list = []
x = N
while i <= N:
    if N % i == 0:
        list.append(i)
        N //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {x} => {list}") 