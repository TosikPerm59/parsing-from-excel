"""
Программа для вычисления позиций ювелирных изделий, находящихся на специальном учете системы ГИИС ДМДК,
в накладных созданных платформой КонтурМаркет. Программа возвращает позиции которые встречаются одновременно,
в накладных КонтурМаркета и накладных платформы ГИИС ДМДК.
"""
from servise_files import reportСreator, giisParser, dirParser, matchСhecker

print('\n', 'Вас приветствует мастер проверки Excel файлов содержащих сведения платформы ГИИС ДМДК.', '\n')

path_to_giis_file = input('Укажите путь к файлу, содержащему сведения ГИИС ДМДК: ')

print()

path_to_invoices = input('Укажите директорию проверяемых файлов Excel: ')

normalized_giis_file = giisParser.giis_file_parsing(path_to_giis_file)
# Парсинг файла Excel, созданого платформой ГИИС ДМДК

normalized_invoices = dirParser.directory_parsing(path_to_invoices)
# Парсинг, анализ и помещение в список накладных созданных КонтурМаркетом

report_list = []

for invoice in normalized_invoices:
    report = matchСhecker.match_checking(normalized_giis_file, invoice)
    # Проверка на совпадение позиций

    report_list.append(report)

reportСreator.create_report_file(report_list)
# Создание файла отчета
