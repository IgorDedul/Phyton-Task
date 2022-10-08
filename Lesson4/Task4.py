# Задача №4: Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

print("Формирует случайным образом список коэффициентов (значения от 0 до 100) и записывает в файл многочлен степени k.")

import random

def write_file(st):
    with open('Task4.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0,101)


def create_mn(k):
    list = [rnd() for i in range(k+1)]
    return list
    

def create_str(sp):
    list= sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i+1] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
write_file(create_str(create_mn(k)))
print("Могочлен записан в файл Task4.txt")