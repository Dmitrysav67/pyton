# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

n = input('Введите число: ')
sum = sum(map(int, n))
print (sum)

n = input('Введите число: ')
sum = 0
for i in n:
  sum += int(i)
print(sum)