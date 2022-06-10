from validity import check_file_path


def input_giis_file_path():
    # giis_file_path = input('Укажите путь к файлу, содержащему сведения ГИИС ДМДК: ').replace('"', '')
    giis_file_path = "E:\Elena\Downloads\\batches_list.xlsx"
    return giis_file_path


def input_folder_path():
    folder_path = input('Укажите директорию проверяемых накладных: ').replace('"', '')
    return folder_path


def input_invoice_path():
    invoice_path = None
    while not invoice_path:
        print('Введите путь к накладной которую хотите изменить или 0 для возврата к основному меню.')
        invoice_path = (input('Введите путь: ')).replace('"', '')
        if str(invoice_path) == '0':
            return invoice_path
        if check_file_path(invoice_path):
            return invoice_path
        else:
            print('\n', 'Путь к файлу не корректен, или файл не является документом WORD', '\n')
            invoice_path = None