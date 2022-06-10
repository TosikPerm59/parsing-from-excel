""" Программа для вычисления позиций ювелирных изделий, находящихся на специальном учете системы ГИИС ДМДК,
в накладных созданных платформой КонтурМаркет. Программа возвращает позиции которые встречаются одновременно,
в накладных КонтурМаркета и накладных платформы ГИИС ДМДК. """

from time import sleep
from servise_files import (giisParser, dirParser, matchСhecker, change_invoice, validity)
from inputs import input_giis_file_path, input_invoice_path, input_folder_path
from validity import check_id


def update_invoice():
    invoice_path = None
    while not invoice_path:
        print('\n', 'Вы выбрали редактирование накладной.', '\n')
        invoice_path = input_invoice_path()
        if str(invoice_path) == '0':
            return

        elif validity.check_invoice(invoice_path):
            change_invoice.change(invoice_path)
        else:
            print('Этот файл не явлется накладной.')
            invoice_path = None


def find_matches():
    print('\n', 'Вы выбрали поиск соответствий')
    giis_file_path = input_giis_file_path()
    folder_path = input_folder_path()
    giis_list = giisParser.giis_file_parsing(giis_file_path)
    invoices_list = dirParser.directory_parsing(folder_path)
    matchСhecker.match_checking(giis_list, invoices_list)


def find_uin():
    print('\n', 'Вы выбрали поиск UIN')
    giis_file_path = input_giis_file_path()
    search_id = None
    while not check_id(search_id):
        search_id = check_id(input('Введите id изделия, по которому нужно найти UIN или 0 для выхода из поиска.'
                                   '(id должен состоять из 13 цифр): '))

        if search_id == '0':
            break
    if search_id == '0':
        return
    giis_list = giisParser.giis_file_parsing(giis_file_path)

    while search_id != '0':
        counter = 0
        result = None

        for giis_dict in giis_list:
            counter += 1
            for giis_key, giis_values in giis_dict.items():
                for item_key, item_value in giis_values.items():
                    if 'ID' in item_key:
                        if search_id == giis_values['ID']:
                            result = giis_key
                            print(f'\nСовпадение найдено в {counter} строке.')
                            print(f'для {search_id} UIN = {result}\n')
                            break
                if result:
                    break
            if result:
                break
        if not result:
            print(f'\nПозиций с id = {search_id} не найдено.\n')

        search_id = None
        while not check_id(search_id):
            search_id = check_id(input('Введите следуйщий ID или 0 для выхода из поиска.'
                                       '(id должен состоять из 13 цифр): '))
            if search_id == '0':
                break
        if search_id == '0':
            return


def prepare_an_invoice():
    print('\n', 'Вы выбрали подготовку входящей накладной для загрузки ее в КонтурМаркет')


act = ''
actions_dict = {'1': ['Редактировать накладную, добавлением в нее цены за грамм, отдельные поля вес и размер',
                      update_invoice],
                '2': ['Найти соответствия изделий в накладных и в базе ГИИС ДМДК', find_matches],
                '3': ['Найти UIN для изделия', find_uin],
                '4': ['Подготовить входящую накладную, для загрузки ее в КонтурМаркет', prepare_an_invoice]}

print('\n', 'Добро пожаловать в мастер помощи с документами системы ГИИС ДМДК.', '\n')

while act != '0':
    print('\n', 'Какое действие вы хотите выполнить?', '\n')
    sleep(1)
    for key, value in actions_dict.items():
        print(f'{key} - {value[0]}\n')
    sleep(1)
    print('Введите цифру соответствующую желаемому действию или 0(ноль)  для завершения программы.')
    act = input('Введите цифру: ')
    if act == '0' or not act.isdigit():
        continue
    elif act not in actions_dict.keys():
        continue
    else:
        actions_dict[act][1]()
