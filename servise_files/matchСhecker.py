
def match_checking(giis_list, invoices_list):
    counter = 0
    for invoice in invoices_list:
        for invoice_key, invoice_values in invoice.items():
            match_dict = {}
            match_dict[invoice_key] = []
            for position in invoice_values:

                for position_key, position_values in position.items():

                    for giis_position in giis_list:

                        for giis_pos_key, giis_pos_values in giis_position.items():
                            matching_counter = 0
                            match_list = []
                            if giis_pos_values['Масса'] == position_values['Масса']:
                                matching_counter += 1
                                match_list.append('Масса')
                            if 'Артикул' in giis_pos_values.keys() and giis_pos_values['Артикул'] == position_key:
                                matching_counter += 1
                                match_list.append('Артикул')
                            if giis_pos_values['Описание'] == position_values['Описание']:
                                matching_counter += 4
                                match_list.append('Полное описание')
                            else:
                                split_descr_giis = giis_pos_values['Описание'].split(',')
                                split_descr_inv = position_values['Описание'].split(',')
                                for element in split_descr_inv:
                                    if element in split_descr_giis:
                                        matching_counter += 1
                                        index = split_descr_inv.index(element)
                                        if index == 0:
                                            match_list.append('Имя')
                                        elif index == 1:
                                            match_list.append('Металл')
                                        elif split_descr_inv[index].startswith(' с '):
                                            match_list.append('Вставка')
                                        elif split_descr_inv[index].startswith(' плетение '):
                                            match_list.append('Плетение')
                                        elif split_descr_inv[index].endswith('р-р'):
                                            match_list.append('Размер')

                            if matching_counter > 2 and len(match_list) > 1:
                                counter += 1
                                if 'Масса' in match_list:
                                    if matching_counter == 6:
                                        print(*giis_position.items(), *position.items(), sep='\n')
                                        print("\033[32m\033[1m\033[7m {}" .format(f'True найдено {matching_counter} '
                                                                                  f'совпадения: {tuple(match_list)}'))
                                        print("\033[0m {}" .format(''))

                                    else:
                                        print(*giis_position.items(), *position.items(), sep='\n')
                                        print("\033[33m\033[1m {}".format(
                                            f'True найдено {matching_counter} совпадения: {tuple(match_list)}'))
                                        print("\033[0m {}".format(''))

    print(f'Всего найдено {counter} близких по содержанию позиций.')



