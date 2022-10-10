#5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import sympy
x = sympy.Symbol('x')

file1 = 'task5_1.txt'
file2 = 'task5_2.txt'

def read_pol(file):  # Получение данных из файла
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

pol1 = read_pol(file1)
pol2 = read_pol(file2)
print('Исходные полиномы:')
print(pol1)
print(pol2)

sum_pol = sympy.simplify(pol1+"+"+pol2)

print('Итоговый результат сложения полиномов:\n', sum_pol)
with open('task5.txt', 'w') as file_sum:
    file_sum.writelines(str(sum_pol))