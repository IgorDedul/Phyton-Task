# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# 
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

print('Данная программа определяет номер четверти плоскости, в которой находится заданная координатами точка')
x = int(input('Введите координату x: '))
y = int(input('Введите координату y: '))
if x > 0 and y > 0:
    print('Заданная точка находится в первой четверти')
if x < 0 and y > 0:
    print('Заданная точка находится во второй четверти')
if x < 0 and y < 0:
    print('Заданная точка находится в третьей четверти')
if x > 0 and y < 0:
    print('Заданная точка находится в четвертой четверти')