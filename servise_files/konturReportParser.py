import openpyxl
from servise_files import excelReader

def kontur_file_parsing(kontur_report_path):
    rows_list, sheet, file_type, file_name, file_path = excelReader.read_excel_file(kontur_report_path)
    group = 'excel'
    kontur_report_dict = {}
    counter = 0
    for row in rows_list[1:]:
        counter += 1
        count = sheet[row][6].value
        count = int(float(count.replace(',', '.'))) if count.find(',') else count
        kontur_report_dict[counter] = {'description': sheet[row][5].value, 'count': count}
    print(f'Сформирован список изделий содержащихся отчете Контура из {counter} позиций.')
    return kontur_report_dict
