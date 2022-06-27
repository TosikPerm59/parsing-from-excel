""" Программа для вычисления позиций ювелирных изделий, находящихся на специальном учете системы ГИИС ДМДК,
в накладных созданных платформой КонтурМаркет. Программа возвращает позиции которые встречаются одновременно,
в накладных КонтурМаркета и накладных платформы ГИИС ДМДК. """

from time import sleep
from servise_files import giisParser, dirParser, matchСhecker, invoiceChanger, invoiceParser
from inputs import input_giis_file_path, input_invoice_path, input_folder_path, input_id
from validity import check_outgoing_invoice
from allFinders import find_uin


def update_outgoing_invoice():
    print('\nВы выбрали редактирование исходящей накладной.\n')
    invoice_path = input_invoice_path(text=' которую хотите изменить')
    if str(invoice_path) == '0':
        return
    elif check_outgoing_invoice(invoice_path):
        invoiceChanger.change_invoice(invoice_path)
    else:
        print('\nЭтот файл не явлется накладной или не является исходящей накладной или '
              'не является документом Word.')
        sleep(3)
        update_outgoing_invoice()


def find_matches():
    print('\nВы выбрали поиск соответствий.\n')
    giis_file_path = input_giis_file_path()
    folder_path = input_folder_path(text=' содержащей исходящие накладные')
    if str(folder_path) == '0':
        return
    elif 'Документы  Александрова Е.П\Накладные\Исходящие накладные' in folder_path:
        giis_list = giisParser.giis_file_parsing(giis_file_path)
        invoices_list = dirParser.directory_parsing(folder_path)
        matchСhecker.match_checking(giis_list, invoices_list)
    else:
        print('\nЭтот путь, не является путем к исходящим накладным.')
        sleep(3)
        find_matches()


def search_uin():
    print('\nВы выбрали поиск UIN в списке изделий содержащихся в ГИИС.\n')
    giis_file_path = input_giis_file_path()
    search_id = input_id()
    if search_id == '0':
        return
    else:
        giis_list = giisParser.giis_file_parsing(giis_file_path)
        uin, counter = find_uin(search_id, giis_list)
        if uin is not None:
            print(f'\nСовпадение найдено в {counter} строке списка ГИИС .')
            print(f'для id = {search_id}, UIN = {uin}\n')
        else:
            print(f'\nПозиций с id = {search_id} не найдено.\n')
        sleep(3)
        search_uin()


def prepare_an_invoice():
    print('\nВы выбрали подготовку входящей накладной для загрузки ее в КонтурМаркет\n')
    invoice_path = input_invoice_path(text=' которую будем готовить для загрузки в КонтурМаркет')
    if str(invoice_path) == '0':
        return
    else:
        invoiceParser.invoice_parsing(invoice_path)


act = ''
actions_dict = {'1': ['Редактировать накладную, добавлением в нее цены за грамм и отдельного поля вес',
                      update_outgoing_invoice],
                '2': ['Найти совпадения изделий в накладных и в базе ГИИС ДМДК', find_matches],
                '3': ['Найти UIN для изделия из накладной ГИИС', search_uin],
                '4': ['Подготовить входящую накладную, для загрузки ее в КонтурМаркет', prepare_an_invoice]}

print('\nДобро пожаловать в мастер помощи с документами системы ГИИС ДМДК.')

while act != '0':
    print('\nКакое действие вы хотите выполнить?', '\n')
    for key, value in actions_dict.items():
        print(f'{key} - {value[0]}')
    print('\nВведите цифру соответствующую желаемому действию или 0(ноль)  для завершения программы.')
    act = input('Выберите действие : ')
    if act == '0' or not act.isdigit():
        continue
    elif act not in actions_dict.keys():
        continue
    else:
        actions_dict[act][1]()
