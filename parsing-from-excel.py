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
for row in range(1, sheet.max_row + 1):
    giis_dict[sheet[row][0].value] = ({'UIN': sheet[row][1].value, 'Наименование': sheet[row][2].value,
                                       'Описание': sheet[row][3].value, 'Масса': sheet[row][4].value,
                                       'Металл': sheet[row][5].value})

print(giis_dict)

input('Press ENTER to exit')
