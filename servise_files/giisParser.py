import openpyxl
import warnings

warnings.simplefilter("ignore")


def giis_file_parsing(path_to_giis_file):

    """ Функция анализа файла Excel сформированного платформой ГИИС ДМДК.
      На вход функция принимает путь к файлу, который необходимо обработать. Так как, данные из портала ГИИС ДМДК
    заполняются разными людьми, то и формат записи и порядок заполнения не имеет четкой последовательности. Для того
    что бы все позиции имели структурированные характеристики, функция проходит построчно по таблице
    и анализируя данные принимает решение о помещении этих данных соответствующим ключам словаря принадлежащего
    текущей позиции.
      Функция возвращает словарь с позициями в которых все характеристики упорядочены и проверены. """

    file_giis = openpyxl.open(path_to_giis_file)

    sheet = file_giis.active
    sheet.delete_rows(1, 3)
    giis_dict = {}

    def find_ID(*description):

        """ Функция ищет в описании и наименовании позиции, строку состоящую из 13 символов и состоящую
        только из цифр.
          Возвращает строку, если она найдена, либо 0. """

        for elem in description:
            elem = str(elem)
            for part in elem.split(' '):
                if len(part) == 13 and part.isdigit():
                    return part

    def find_art(*args):

        """ Функция анализирует столбцы Описание и Наименование, находит и проверяет артикул позиции
          Возвращает артикул, если он найден или 0. """

        prefixes = ['НЦ', 'ЦБ', 'ЦИ', 'ББ', 'БВ', 'БИ', 'БК', 'НБ']
        word_exceptions = ['585-й', '925-й', '0070', '585']

        def word_exceptions_check(_string):

            """ Функция проверяет наличие слов исключений в передаваемой строке.
            Возвращает False в случае наличия слов исключений в строке или True при отсутствии """

            for exception in word_exceptions:
                if exception in _string:
                    return False
            else:
                return True

        for elem in args:
            elem = str(elem).split(' ')

            for pos in range(len(elem)):
                if elem[pos] in prefixes:
                    return elem[pos] + ' ' + elem[pos + 1]

                elif elem[pos] == 'Арт.':
                    return elem[pos + 1]

                elif 'перлина' in elem[pos]:
                    elem_lst = list(elem[pos])
                    for simbol in 'перлина':
                        elem_lst.remove(simbol)
                    return ''.join(elem_lst)

                elif ((elem[pos].isdigit() or elem[pos].isalnum()) and 2 < len(elem[pos]) != 13 and
                      not elem[pos].isalpha() and word_exceptions_check(elem[pos])):
                    return elem[pos]

                elif ('-' in elem[pos] or '_' in elem) and word_exceptions_check(elem[pos]):
                    return elem[pos]

    def find_description(*args):

        """ Функция анализирует столбцы Описание, Наименование и Основной металл, находит и составляет описание
         позиции.
          Возвращает описание позиции, если оно найдено или 0. """

        description = ''
        keywords_name = ['кольцо', 'цепь', 'серьги', 'подвеска', 'пуссеты', 'браслет', 'крест', 'икона']
        keywords_inserts = {'аметистом': 'с аметистом', 'топазом': 'с топазом', 'аметрином': 'с аметрином',
                            'празолитом': 'с празолитом', 'агатом': 'с агатом', 'гранатом':'с гранатом',
                            'фианит': 'с фианитом', 'турмалин': ' с турмалином', 'Лондон': 'с топазом Лондон'}

        for elem in args[:2]:
            elem = str(elem)

            if description == '':
                for keyword in keywords_name:
                    if keyword in elem.lower():
                        description = keyword.capitalize() + ' ' + args[2].capitalize() + ' ' + args[3]
                        break

            elif len(description.split()) == 3:
                for key in keywords_inserts.keys():
                    if key in elem:
                        description = description + ' ' + keywords_inserts[key]

                split_element = elem.split(' ')
                if 'р.' in elem:
                    size = str(split_element[(split_element.index('р.') + 1)][:-1])
                    description = description + ',' + ' р-р ' + size

        return description

    for row in range(1, sheet.max_row + 1):  # Выполняется построчный проход по таблице
    # for row in range(50, 58): #  Test
        # print(f'строка № {sheet[row][0].value}, описание {sheet[row][2].value}, {sheet[row][3].value}')
        giis_dict[sheet[row][0].value] = {
            'uin': sheet[row][1].value if sheet[row][1].value.isdigit() and len(sheet[row][1].value) == 16 else 0,
            'id': find_ID(sheet[row][2].value, sheet[row][3].value),
            'Артикул': find_art(sheet[row][2].value, sheet[row][3].value),
            'Описание': (find_description(sheet[row][2].value, sheet[row][3].value, sheet[row][5].value,
                                          sheet[row][7].value)),
            'Масса': sheet[row][4].value + 'г.',
            'Металл': sheet[row][5].value + ' ' + sheet[row][7].value + ' пробы'
        }

    print(*((key, value) for key, value in giis_dict.items()), sep='\n')


# giis_file_parsing(r"E:\Elena\Downloads\batches_list (1).xlsx")  # True example
# giis_file_parsing(r"E:\Elena\Downloads\batches_list (1) — копия.xlsx")  # False example
giis_file_parsing(r"E:\Elena\Downloads\batches_list (2).xlsx")  # True example