

def find_uin(search_id, giis_list):
    counter = 0
    result = None
    for giis_dict in giis_list:
        counter += 1
        for giis_key, giis_values in giis_dict.items():
            for item_key, item_value in giis_values.items():
                if 'ID' in item_key:
                    if search_id == giis_values['ID']:
                        result = giis_key
                        print(f'\nСовпадение найдено в {counter} строке списка ГИИС .')
                        print(f'для id = {search_id}, UIN = {result}\n')
                        break
            if result:
                break
        if result:
            break
    if not result:
        print(f'\nПозиций с id = {search_id} не найдено.\n')
