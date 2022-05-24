""" Программа для вычисления позиций ювелирных изделий, находящихся на специальном учете системы ГИИС ДМДК,
в накладных созданных платформой КонтурМаркет. Программа возвращает позиции которые встречаются одновременно,
в накладных КонтурМаркета и накладных платформы ГИИС ДМДК. """

from servise_files import giisParser, dirParser, matchСhecker, reportСreator, handlerFunctions


print('\n', 'Вас приветствует мастер проверки Excel файлов содержащих сведения платформы ГИИС ДМДК.', '\n')

# path_to_giis_file = input('Укажите путь к файлу, содержащему сведения ГИИС ДМДК: ')
path_to_giis_file = "E:\Elena\Downloads\\batches_list (2).xlsx"
print()

# path_to_invoices = input('Укажите директорию проверяемых накладных: ')
path_to_invoices = "E:\Elena\Desktop\Документы  Александрова Е.П\Накладные Кирпичникова Маргарита"

print()

# Парсинг файла Excel, созданого платформой ГИИС ДМДК
giis_list = giisParser.giis_file_parsing(path_to_giis_file)


# Парсинг, анализ и помещение в список накладных созданных КонтурМаркетом
invoices_list = dirParser.directory_parsing(path_to_invoices)

# Проверка на совпадение позиций

report_list = matchСhecker.match_checking(giis_list, invoices_list)

# Создание файла отчета
# reportСreator.create_report_file(report_list)

# print('Список изделий содержащихся в накладной ГИИС ДМДК')
# print()
# for i in giis_list:
#     print(i.items())
#
# print()
#
# print('Список изделий в накладных:')
#
# for dictionaries in invoices_list:
#     for key, values in dictionaries.items():
#         print()
#         print(key)
#         print()
#         for value in values:
#             print(value)



