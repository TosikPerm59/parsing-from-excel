""" Программа для вычисления позиций ювелирных изделий, находящихся на специальном учете системы ГИИС ДМДК,
в накладных созданных платформой КонтурМаркет. Программа возвращает позиции которые встречаются одновременно,
в накладных КонтурМаркета и накладных платформы ГИИС ДМДК. """

from servise_files import reportСreator, giisParser, dirParser, matchСhecker

print('\n', 'Вас приветствует мастер проверки Excel файлов содержащих сведения платформы ГИИС ДМДК.', '\n')

path_to_giis_file = input('Укажите путь к файлу, содержащему сведения ГИИС ДМДК: ')

print()

path_to_invoices = input('Укажите директорию проверяемых файлов Excel: ')

# Парсинг файла Excel, созданого платформой ГИИС ДМДК
normalized_giis_dict = giisParser.giis_file_parsing(path_to_giis_file)

# Парсинг, анализ и помещение в список накладных созданных КонтурМаркетом
normalized_invoices = dirParser.directory_parsing(path_to_invoices)

report_list = []

# Проверка на совпадение позиций
for invoice in normalized_invoices:
    report = matchСhecker.match_checking(normalized_giis_dict, invoice)

    report_list.append(report)

# Создание файла отчета
reportСreator.create_report_file(report_list)
