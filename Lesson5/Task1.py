#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
#За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def input_bot(value):
    if value < 29: x = value
    elif value < 58 and value > 29: x = value - 29
    elif value < 86 and value > 57: x = value - 57
    else: x = randint(1,29)
    return x

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

print ("Перед вами игра. На столе лежит оределенное число конфет. Каждый игрок может взять от 1 до 28 конфет. Выиграет тот, кто заберет последние конфеты.")
player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока или напишите bot если хотите играть с компьютером: ")
value = int(input("Введите количество конфет на столе: "))

print ("По результату жеребьевки:")
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 0:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        if player2 == 'bot': k = input_bot(value)
        else: k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player2}")
else:
    print(f"Выиграл {player1}")
print("и забирает все ", counter1+counter2, " конфет.")