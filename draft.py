import openpyxl
import warnings
import os
warnings.simplefilter("ignore")

adress_file_from_giis = ('E:\Elena\Downloads\/' +
    (input('Ведите название файла Excel скачанного с ГИИС ДМДК (файл должен находиться в папке загрузки): ')))

file_giis = openpyxl.open(adress_file_from_giis)

sheet = file_giis.active
sheet.delete_rows(1, 3)
giis_dict = {}

def check_number(st):
    true_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in st:
        if i not in true_lst:
            return False
    else:
        return True


def check_description(self, description):
    for elem in description.split(' '):
        if len(elem) == 13:
            if check_number(elem):
                self.value[id] = elem



class Jewelry:
    def init(self, name, description, weight, metall):
        pass




for row in range(1, sheet.max_row + 1):
    giis_dict[sheet[row][0].value] = ({'UIN': sheet[row][1].value, 'Наименование': sheet[row][2].value,
                                       'Описание': sheet[row][3].value, 'Масса': sheet[row][4].value,
                                       'Металл': sheet[row][5].value})

for elem in giis_dict.values():
    print(elem)


def check_number(str_check):
    true_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in str_check:
        if i not in true_lst:
            return False
    else:
        return True


def check_description(self, description):
    description_lst = description.split(' ')
    desc_dict = {}
    for elem in description_lst:
        if len(elem) == 13:
            if check_number(elem):
                self.values[id] = elem
        if elem == 'Арт.' or elem == 'арт.':
            self[artic] = (description_lst[(description_lst.index(elem)) + 1].split(','))[0]
    return desc_dict



print(check_description('Арт. 018181-1102, р. 17,5, вставки - 21 Фианит Кр 1,00 0,036 Бесцветный 9115017603784'))