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


