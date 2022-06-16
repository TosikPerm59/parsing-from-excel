import xlrd


def excel_file_parsing(path_to_excel_file):
    excel_file = xlrd.open_workbook(path_to_excel_file)
    sheet = excel_file.sheet_by_index(0)
    rows_list = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    product_ind = weight_ind = price_ind = start = finish = None
    for row in rows_list:
        if 'Страница 1' in row:
            start = rows_list.index(row) + 1
        row.remove('')
        if 'Всего по накладной ' in row:
            finish = rows_list.index(row) - 1
            break

    header = rows_list[start: start + 2]
    for row in header:

        r_elem = None
        for elem in row:
            r_elem = elem.replace('\n', '')
            if r_elem.find('наименование') != -1:
                product_ind = row.index(elem)
            if r_elem.find('нетто') != -1:
                weight_ind = row.index(elem)
            if r_elem.find('Сумма сучетом НДС') != -1:
                price_ind = row.index(elem)

    raw_product_list = []

    for row in rows_list[start: finish]:
        if isinstance(row[0], float):
            raw_product_list.append(row)

    product_list = []

    for product in raw_product_list:
        print(product)

        # prod_uin =
        # prod_name
        # prod_metal
        # prod_descr
        # prod_weight
        # prod_art
        # prod_price


excel_file_parsing('E:\Elena\Downloads\\100 Алёна.xls')
