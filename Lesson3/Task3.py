#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print('Программа вычисляет разницу между максимальным и минимальным значением дробной части элементов.')

size = int(input('Какое количество элементов вы хотите добавить список? Укажите число или поставьте 0 если хотите использовать заданный список: '))

if size == 0:
    list = [1.1, 1.2, 3.1, 5, 10.01]
elif size > 0:
    list = []
    for i in range (1, size + 1):
        list.append(float(input(f'Задайте {i} элемент: ')))
else: print('Ошибка ввода.')

print('Заданный список', list)

new_list = []
for i in list:
    if i%1 != 0:
        new_list.append(round(i%1,2))

result = round(max(new_list) - min(new_list),2)
print('Разница между максимальным', max(new_list), 'и минимальным', min(new_list), 'значениями дробной части элементов равна', result)