import os
import docx
from allFinders import find_art, find_description, find_weight
from validity import check_file_path


def docxParser(path):

    """ Функция извлечения данных из документа типа 'docx'. Построчно перебирает таблицу документа. Создает словари, где
     ключ, артикул изделия, а значения, описание изделия. Извлекает из строк описание изделия и добавляет их в
     словарь. Затем добавляет словари в список.
     Возвращает список словарей. """

    document = docx.Document(path)
    max_row = (len(document.tables[1].rows))
    group = 'word'
    art_list = []

    # Построчный проход по таблице накладной
    for i in range(3, max_row - 21):
        _string = document.tables[1].rows[i].cells[4].text
        print(_string)
        split_string = _string.lower().split(' ')
        art = find_art(_string, group=group)
        art_dict = {find_art(_string, group=group): {}}
        art_dict[art]['Описание'] = find_description(split_string, group=group)
        art_dict[art]['Масса'] = str(find_weight(split_string)) + ' гр'

        art_list.append(art_dict)

    return art_list


def pdfParser(path, file):
    pass


def directory_parsing(path_to_invoices):

    """ Функция проходит по всем файлам и папкам находящимся в указанной директории, проверяет их на причастность к
    накладным и запускает для каждого подходящего файла парсеры соответствующие формату файла.  """

    file_list = []
    file_dict = {}
    # Проход по файлам указанной директории

    if check_file_path(path_to_invoices):
        file_dict[path_to_invoices] = docxParser(path_to_invoices)
        file_list.append(file_dict)
    else:
        for root, dirs, files in os.walk(path_to_invoices):

            for file in files:

                if file.startswith('~'):
                    continue

                path = path_to_invoices + '\\' + file

                if check_file_path(path) and file.endswith('.docx'):
                    print(file)
                    file_dict[file] = docxParser(path)
                    file_list.append(file_dict)

    for i in file_list:
        for key, values in i.items():
            print(key)
            counter = 0
            for value in values:
                counter += 1
                print(f'Строка {counter} === {value}')
    return file_list


# directory_parsing("E:\Elena\Desktop\Документы  Александрова Е.П\Накладные Кирпичникова Маргарита")
# directory_parsing('E:\Elena\Documents\Документы  Александрова Е.П\Накладные\Исходящие накладные\Накладные Каурова Евгения')
# directory_parsing("E:\Elena\Desktop\Документы  Александрова Е.П\Накладные Сартакова Светлана")

# docxParser("E:\Elena\Documents\Документы  Александрова Е.П\Накладные\Исходящие накладные\Накладные Дульцева Анна\Расходная_накладная_№25_от_05-06-22.docx")