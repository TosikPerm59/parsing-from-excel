import openpyxl
import warnings
from os import path
from handlerFunctions import find_art, find_description, find_weight
import handlerFunctions

warnings.simplefilter("ignore")


def find_id(*description):

    """ Функция ищет в описании и наименовании позиции, строку состоящую из 13 символов и состоящую
    только из цифр.
        Возвращает строку или None """

    for elem in description:
        elem = str(elem)
        for part in elem.split(' '):
            if len(part) == 13 and part.isdigit():
                return part


def giis_file_parsing(path_to_giis_file):

    """ Функция анализа файла Excel сформированного платформой ГИИС ДМДК.
      На вход функция принимает путь к файлу, который необходимо обработать. Так как, данные из портала ГИИС ДМДК
    заполняются разными людьми, то и формат записи и порядок заполнения не имеет четкой последовательности. Для того
    что бы все позиции имели структурированные характеристики, функция проходит построчно по таблице
    и анализируя данные принимает решение о помещении этих данных соответствующим ключам словаря принадлежащего
    текущей позиции.
      Функция возвращает словарь с позициями в которых все характеристики упорядочены и проверены. """
    path_to_giis_file = path_to_giis_file.replace('"', '')
    file_giis = openpyxl.open(path_to_giis_file, keep_vba=False)
    giis_list = []
    sheet = file_giis.active
    sheet.delete_rows(1, 3)
    group = 'excel'

    # Выполняется построчный проход по таблице
    for row in range(1, sheet.max_row + 1):
    # for row in range(11, 13): #  Test variant
        # strings_2_3 = sheet[row][2].value, sheet[row][3].value
        uin = sheet[row][1].value
        _id = find_id(sheet[row][2].value, sheet[row][3].value)
        art = find_art(sheet[row][2].value, sheet[row][3].value, group=group)
        descr = find_description(sheet[row][2].value, sheet[row][3].value, sheet[row][5].value,
                                 sheet[row][7].value, group=group)
        weight = find_weight(sheet[row][4].value, group)

        giis_dict = {uin: {}}
        if _id:
            giis_dict[uin]['ID'] = _id
        if art:
            giis_dict[uin]['Артикул'] = art

        giis_dict[uin]['Описание'] = descr
        giis_dict[uin]['Масса'] = weight + ' гр'

        giis_list.append(giis_dict)

    # for i in giis_list:
    #     print(i.items())
    return giis_list


# Testing
# giis_file_parsing(r"E:\Elena\Downloads\batches_list (1).xlsx")  # True example
# giis_file_parsing(r"E:\Elena\Downloads\batches_list (1) — копия.xlsx")  # False example
# giis_file_parsing(r"E:\Elena\Downloads\batches_list (2).xlsx")  # True example
