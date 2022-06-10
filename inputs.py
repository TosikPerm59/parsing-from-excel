from validity import check_file_path, check_path, check_id


def while_for_inputs(check_func, descr_print, input_print, error_print):
    variable = None
    while not variable:
        print(descr_print)
        variable = input(input_print)
        if '"' in variable:
            variable = variable.replace('"', '')
        if variable[-1] == ' ':
            variable = variable[-1]
        if check_func(variable) or str(variable) == '0':
            return variable
        else:
            print(f'\n{error_print}\n')
            variable = None


def input_giis_file_path():
    # giis_file_path = input('Укажите путь к файлу, содержащему сведения ГИИС ДМДК: ').replace('"', '')
    giis_file_path = "E:\Elena\Downloads\\batches_list.xlsx"
    return giis_file_path


def input_folder_path(text=''):
    check_func = check_path
    descr_print = f'Введите путь к папке{text} или 0 для возврата к основному меню.'
    input_print = 'Введите путь: '
    error_print = 'Путь к папке не корректен.'
    return while_for_inputs(check_func, descr_print, input_print, error_print)


def input_invoice_path(text=''):
    check_func = check_file_path
    descr_print = f'Введите путь к накладной{text} или 0 для возврата к основному меню.'
    input_print = 'Введите путь: '
    error_print = 'Путь к файлу не корректен.'
    return while_for_inputs(check_func, descr_print, input_print, error_print)


def input_id():
    check_func = check_id
    descr_print = 'Введите id изделия, по которому нужно найти UIN или 0 для выхода из поиска.'
    input_print = 'Введите id: '
    error_print = 'Не корректный id.(id должен состоять из 13 цифр)'
    return while_for_inputs(check_func, descr_print, input_print, error_print)

