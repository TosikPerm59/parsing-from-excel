from openpyxl import Workbook
from allFinders import *
from servise_files import giisParser, excelReader
from inputs import input_giis_file_path


def invoice_parsing(path_to_excel_file):

    rows_list, sheet, file_type, file_name, file_path = excelReader.read_excel_file(path_to_excel_file)
    product_ind = weight_ind = price_ind = prod_uin = start = finish = price_per_gram_ind = None
    new_excel_file = Workbook()
    new_excel_sheet = new_excel_file.active
    products_with_size = {'кольцо': 'кольца', 'цепь': 'цепи', 'браслет': 'браслета', 'колье': 'колье'}

    if file_type == '.xls':
        for row in rows_list:
            if 'Страница 1' in row:
                start = rows_list.index(row) + 1
            if row[0] == '':
                row.remove('')
            if 'Всего по накладной ' in row:
                finish = rows_list.index(row) - 1
                break

        header = rows_list[start: start + 2]

        for row in header:

            for elem in row:
                r_elem = elem.replace('\n', '')
                if r_elem.find('наименование') != -1:
                    product_ind = row.index(elem)
                if r_elem.find('нетто') != -1:
                    weight_ind = row.index(elem)
                if r_elem.find('Сумма сучетом НДС') != -1:
                    price_ind = row.index(elem)
                if r_elem.find('Цена') != -1:
                    price_per_gram_ind = row.index(elem)

        raw_product_list = []

        for row in rows_list[start: finish]:
            if isinstance(row[0], float):
                raw_product_list.append(row)

        giis_list = giisParser.giis_file_parsing(input_giis_file_path())
        counter = 0

        for product in raw_product_list:
            counter += 1
            description_string = product[product_ind].lower()

            prod_name = find_name(description_string)
            prod_metal = find_metal(description_string)
            prod_size = find_size(description_string, group='excel')
            prod_weight = product[weight_ind]
            prod_art = find_art(description_string, group='excel')
            prod_barcode = find_barcode(description_string)
            prod_price = product[price_ind]

            if not prod_metal:
                if product[price_per_gram_ind] > 2500:
                    prod_metal = 'Золото 585'
                else:
                    prod_metal = 'Серебро 925'

            product_description = f'{prod_name}, {prod_metal} ('
            if prod_art:
                product_description = f'{product_description}арт. {prod_art}'
            if prod_barcode:
                prod_uin = find_uin(prod_barcode, giis_list)
                if prod_uin:
                    product_description = f'{product_description}, уин {prod_uin}'
            product_description = f'{product_description}, вес {prod_weight} г.'

            if prod_name.lower() in products_with_size.keys():
                if not prod_size:
                    print(f'\nПрограмме не удалось определить размер для {products_with_size[prod_name.lower()]}.')
                    print(f'Укажите размер для изделия: {product_description}')
                    prod_size = input('Введите размер в формате 00.0: ')
            if prod_size:
                product_description = f'{product_description}, р-р {prod_size}'
            product_description = f'{product_description})'
            print(product_description)

            new_excel_sheet['A' + str(counter)] = product_description
            new_excel_sheet['B' + str(counter)] = prod_barcode
            new_excel_sheet['C' + str(counter)] = prod_uin
            new_excel_sheet['D' + str(counter)] = 'Товар'
            new_excel_sheet['E' + str(counter)] = prod_price
            new_excel_sheet['F' + str(counter)] = prod_metal.split(' ')[0]
            new_excel_sheet['G' + str(counter)] = prod_name

            prod_name = prod_metal = prod_inserts = prod_weaving = prod_art = prod_uin = prod_barcode = None

    if file_type == '.xlsx':
        cols = sheet.max_column
        rows_lst = []
        for row in rows_list:
            row_lst = []
            for col in range(cols):
                row_lst.append(sheet[row][col].value)
            rows_lst.append(row_lst)

        for row in rows_lst:
            if 'Страница 1' in row:
                start = rows_lst.index(row) + 1
            if row[0] is None:
                row.remove(None)
            if 'Всего по накладной ' in row:
                finish = rows_lst.index(row) - 1
                break

        header = rows_lst[start: start + 3]
        rows_lst = rows_lst[start + 3: finish]

        counter = 1
        list_r = []
        for row in rows_lst:
            if row[0] == counter:
                list_r.append(row)
                counter += 1

        for row in header:
            print(row)

            for elem in row:
                if elem is not None:
                    origin_elem = elem
                    elem = str(elem).lower()
                    r_elem = ''
                    if '\n' in elem:
                        r_elem = elem.replace('\n', '')

                    if r_elem.find('наименование,') != -1 or elem.find('наименование,') != -1:
                        product_ind = row.index(origin_elem)
                    if r_elem.find('нетто') != -1 or elem.find('нетто,') != -1:
                        weight_ind = row.index(origin_elem)
                    if r_elem.find('сумма сучетом ндс') != -1 or elem.find('сумма сучетом ндс') != -1:
                        price_ind = row.index(origin_elem)
                    if r_elem.find('цена') != -1 or elem.find('цена') != -1:
                        price_per_gram_ind = row.index(origin_elem)

        print(product_ind, weight_ind, price_ind, price_per_gram_ind)

    path_for_save = f'{file_path}\\Номенклатура файла ({file_name}).xlsx'
    # new_excel_file.save(path_for_save)


# invoice_parsing('E:\Elena\Documents\Документы  Александрова Е.П\Накладные\Входящие накладные\Белышева Юлия\Аена 99.xlsx')
