# функция записи данных
def write_new_data(a):
    with open('base.txt', 'a', encoding = 'utf-8') as f:
        f.write(f'{a}')
    print('Данные записаны')
    print()

# функция чтения данных
def read_data():
    with open('base.txt', 'r', encoding = 'utf-8') as f:
        return f.read()

import re
import os

# функция перезаписи данных
def alter(old_str, new_str):
    with open('base.txt', 'r', encoding = 'utf-8') as f1, open('%s.bak' % 'base.txt', 'w', encoding = 'utf-8') as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str, new_str)
            f2.write(line)
    os.remove('base.txt')
    os.rename('%s.bak' % 'base.txt', 'base.txt')
    print('Данные отредактированы')
    print()