# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

number = int(input('Введите число:\n'))
s = 1
for i in range(number):
    i += 1
    s = i * s

print('произведений чисел:', s)