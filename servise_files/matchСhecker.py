from servise_files import giisParser, konturReportParser
from allFinders import find_uin_in_string, find_name, find_weight, find_size, find_metal


def match_checking(giis_list, invoices_list):
    counter = 0
    full_mach_list = []

    for invoice in invoices_list:
        for invoice_key, invoice_values in invoice.items():
            match_dict = {invoice_key: []}
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
                                        full_mach_list.append(giis_position)
                                        print(*giis_position.items(), *position.items(), sep='\n')
                                        print("\033[32m\033[1m\033[7m {}".format(f'True найдено {matching_counter} '
                                                                                 f'совпадения: {tuple(match_list)}'))
                                        print("\033[0m {}".format(''))

                                    else:
                                        print(*giis_position.items(), *position.items(), sep='\n')
                                        print("\033[33m\033[1m {}".format(
                                            f'True найдено {matching_counter} совпадения: {tuple(match_list)}'))
                                        print("\033[0m {}".format(''))

    print(f'Всего найдено {counter} близких по содержанию позиций, из них {len(full_mach_list)} идентичных позиций.')
    print(f'\nСписок идентичных позиций:\n')
    for item in full_mach_list:
        print(*item.items(), end='\n\n')


def product_availability_check():  # giis_list, report_kontur):
    kontur_report_path = "E:\Elena\Downloads\Отчет по поставкам на 23 сентября.xlsx"
    giis_file_path = "E:\Elena\Downloads\\4_BATCH_LIST_PRINT.xlsx"
    giis_list = giisParser.giis_file_parsing(giis_file_path)
    giis_dict = {}
    uin_list = set()
    counter = 0

    for elem_from_giis_list in giis_list:
        for key, value in elem_from_giis_list.items():
            giis_dict[key] = value



    kontur_report_dict = konturReportParser.kontur_file_parsing(kontur_report_path)
    aviable_product_list = set()
    not_aviable_prod_list = {}
    art_set = set()
    sold_product_list = {}
    sold_product_uin_set = set()

    for key, values in kontur_report_dict.items():
        description = ''.join(values['description'].split(','))
        description = description.replace('(', '') if '(' in description else description
        description = description.replace(')', '') if ')' in description else description
        uin = find_uin_in_string(description)
        if uin and values['count'] == 1:
            aviable_product_list.add(uin)

        if uin and values['count'] == 0:
            sold_product_list[uin] = values
    print(f'Сформирован список изделий поправка которых не требуется, всего {len(aviable_product_list)} позиций')
    print(f'Сформирован список изделий имеющих в шапке УИН и имеющих нулевой остаток, всего {len(sold_product_list)}')
    for key, values in giis_dict.items():
        for key_giis, values_giis in sold_product_list.items():
            if key == key_giis:
                print('Изделие с нулевым остатком')
        if key not in aviable_product_list:

            counter += 1

            split_descripton = ''.join(values['Описание'].lower().split(',')).split(' ')

            name = find_name(split_descripton) if find_name(split_descripton) else ''
            metal = find_metal(split_descripton) if find_metal(split_descripton) else ''
            art = values['Артикул'] if 'Артикул' in values.keys() else ''
            art_set.add(art) if art != '' else None
            art = art.replace(',', '') if ',' in art else art
            weight = values['Масса'][:-3]
            size = find_size(split_descripton, group='excel')
            description_string = (f'{name.capitalize()}, {metal.capitalize()} (арт. {art}, уин {key}, вес {weight} г., '
                                  f'р-р {size})' if size else f'{name.capitalize()}, {metal.capitalize()} (арт. {art}, '
                                                              f'уин {key}, вес {weight} г.)')
            not_aviable_prod_list[key] = values
            not_aviable_prod_list[key].update({'description_string': description_string})
            print(key, values)
            print(description_string)
            print()
            print()
    print(f'Всего отображено {counter} позиций')

    for art in art_set:
        for key, values in not_aviable_prod_list.items():
            if 'Артикул' in values.keys():
                if art == values['Артикул']:
                    print(values['ID'] if 'ID' in values.keys() else None)
                    print(values['description_string'])
                    print()
        print()
        print()
    input()




        # if uin and values['count'] == 1:
        #     print(uin, values['count'], values['description'])
        #     if str(uin) in giis_dict.keys():
        #         print(giis_dict[uin])
        #         print(f'Позици удалена из словаря === {giis_dict.pop(str(uin))}')
        #     else:
        #         print('Позиция не найдена в списке ГИИС')
        #         input()

    # print(f'{len(uin_list)} уникальных уинов в Контуре')

    # for uin in list(uin_list):
    #     if uin in giis_dict.keys():
    #         giis_dict.pop(uin)

    # for key, values in giis_dict.items():
    #     counter += 1
    #     description = values['Описание'].lower()
    #     art = values['Артикул'] if 'Артикул' in values.keys() else ''
    #     name = find_name(description) if find_name(description) is not None else ''
    #     metal = find_metal(description) if find_metal(description) is not None else ''
    #     weight = values['Масса']
    #     size = find_size(description.split(','), group='excel')
    #     description = f'{name.capitalize()}, {metal.capitalize()} (арт. {art}, уин {key}, вес {weight}.'
    #     description += f', р-р {size})' if size else ')'
        # if 'ID' in values.keys():
    #         print(values['ID'], end='  ')
    #     print(description)
    # print(f'Всего {counter} позиций.')



