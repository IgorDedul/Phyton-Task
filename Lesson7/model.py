from re import I


def get_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    return f'{name} || {phone} \n'

def find_contact(book, req):
    a = ''
    for i in book:
        if i.find(req) != -1: a = i 
    if a == '': 
        return 'Вы ввели пустой запрос.'
    else: return a

def get_request(): 
    return input('Введите контакт для поиска: ')

def choose_mode():
    return (int(input('Для записи нового телефона, введите 1. Для поиска в справочнике введите 2. Введите 0 для выхода.')))