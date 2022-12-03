#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
x = int(input("Введите число:  "))
a,b= 1,1
list1 = [a, b]
for i in range(2, x):
    a,b = b, a + b
    list1.append(b)
print(list1)
a,b= 1,1
for i in range(-x, 1):
    a,b = b, a - b
    list1.insert(0, b)
print(list1)