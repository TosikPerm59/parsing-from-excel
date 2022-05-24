#
# def word_exceptions_check(_string):
#
#     """ Функция проверяет наличие слов исключений в передаваемой строке.
#     Возвращает False в случае наличия слов исключений в строке или True при отсутствии """
#
#     word_exceptions = ['585-й', '925-й', '0070', '585', '925']
#
#     for exception in word_exceptions:
#         if exception in _string:
#             return False
#     else:
#         return True
#
#
# def isinteger(value):
#
#     """ Функция проверяет элемент на причастность к целому числу.
#     Возвращает boolean """
#
#     try:
#         int(value)
#         return True
#     except ValueError:
#         return False
#
#
# def isfloat(value):
#
#     """ Функция проверяет элемент на причастность к вещественному числу.
#         Возвращает boolean """
#
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False
#
#
# # Варианты возможных размеров изделий
# sizes = ['14.0', '14.5', '15.0', '15.5', '16.0', '16.5', '17.0', '17.5', '18.0', '18.5', '19.0', '19.5', '20.0',
#          '20.5', '21.0', '21.5', '22.0', '22.5', '23.0', '23.5', '24.0', '24.5', '25.0', '30.0', '35.0', '40.0',
#          '45.0', '50.0', '55.0', '60.0', '65.0', '70.0', '75.0']
#
#
# def find_weight(split_string, group):
#
#     """ Функция поиска массы(вес) изделия, перебирает элементы, проверяет их на причастность к числу.
#     Возвращает вещественное число или None"""
#
#     if group == 'word':
#         index = (split_string.index('—') if '—' in split_string else split_string.index('---'))
#         split_right_part = ((' '.join(split_string).split(split_string[index])[1]).split(' '))[1:]
#
#         for elem in split_right_part:
#             if len(elem) > 1:
#                 if not elem[-1].isdigit():
#                     elem = elem[:-1]
#                 if not elem[-1].isdigit():
#                     elem = elem[:-1]
#                 if ',' in elem:
#                     elem.replace(',', '.')
#                 if isfloat(elem):
#                     if elem not in sizes:
#                         return elem
#
#     if group == 'excel':
#         weight = None
#         if ',' in split_string:
#             weight = split_string.replace(',', '.')
#             if len((weight.split('.'))[1]) == 1:
#                 weight = weight + '0'
#         if split_string.isdigit():
#             weight = split_string + '.00'
#
#         return weight
#
#
# def find_art(*args, group):
#
#     """ Функция анализирует столбцы Описание и Наименование, находит и проверяет артикул позиции
#       Возвращает артикул или None. """
#
#     prefixes = ['НЦ', 'ЦБ', 'ЦИ', 'ББ', 'БВ', 'БИ', 'БК', 'НБ']
#
#     for elem in args:
#
#         elem = str(elem).split(' ')
#
#         # Поиск артикула по разным критериям
#         for pos in range(len(elem)):
#             if elem[pos] in prefixes:
#                 return elem[pos] + ' ' + elem[pos + 1]
#
#             elif elem[pos] == 'Арт.':
#                 return elem[pos + 1]
#
#             elif 'перлина' in elem[pos] and group == 'excel':
#                 elem_lst = list(elem[pos])
#                 for simbol in 'перлина':
#                     elem_lst.remove(simbol)
#                 return ''.join(elem_lst)
#
#             elif ((elem[pos].isdigit() or elem[pos].isalnum()) and 2 < len(elem[pos]) != 13 and
#                   not elem[pos].isalpha() and word_exceptions_check(elem[pos])):
#                 return elem[pos]
#
#             elif ('-' in elem[pos] or '_' in elem) and word_exceptions_check(elem[pos]):
#                 return elem[pos]
#
#
# def find_description(*args, group):
#
#     """ Функция анализирует столбцы Описание, Наименование и Основной металл, находит и составляет описание
#         позиции.
#         Возвращает описание позиции. """
#
#     # Варианты префиксов артикула изделия относящегося к цепям или браслетам
#     keywords = {'цепь': ['цб', 'нц', 'ци'], 'браслет': ['бр', 'бк', 'нб', 'бб', 'бв', 'би']}
#
#     # Варианты плетений цепей и браслетов
#     keywords_weaving = {'перлина': ['шариковая', 'перлина'], 'сингапур': ['сингапур'], 'нонна': ['нонна'],
#                         'якорь': ['якорь', 'якорное'], 'бисмарк': ['бисмарк'], 'фигаро': ['фигаро', 'картье'],
#                         'снэйк': ['снэйк', 'снейк', 'кобра'], 'ромб': ['ромб'], 'love': ['love', 'лав', 'сердечки']}
#
#     # Варианты имен изделий
#     keywords_name = ['кольцо', 'цепь', 'серьги', 'подвеска', 'пуссеты', 'браслет', 'крест', 'икона']
#
#     # Варианты вставок в изделия
#     keywords_inserts = {'аметистом': ['аметистом', 'аметист'], 'топазом': ['топазом', 'топаз'],
#                         'аметрином': ['аметрином', 'аметрин'], 'празолитом': ['празолитом', 'празолит'],
#                         'агатом': ['агатом', 'агат'], 'гранатом': ['гранатом', 'гранат'],
#                         'фианитами': ['фианитом', 'фианит', 'фианитами'], 'турмалином': ['турмалином', 'турмалин'],
#                         'топазом Лондон': ['Лондон', 'топаз лондон', 'топазом лондон'],
#                         'ювелирным стеклом': ['стекло', 'ювелирное'], 'ониксом': ['ониксом'],
#                         'наношпинделем': ['наношпиндель']}
#
#     def find_name(split_string):
#
#         """ Метод поиска наименования изделия, сопоставляет содержимое строки со списком вариантов имен.
#         Возвращает имя или None ."""
#
#         for name in keywords_name:
#
#             if name in split_string:
#                 return name.capitalize()
#
#         for keywords_key, keywords_values in keywords.items():
#             for value in keywords_values:
#                 if value in split_string:
#                     return keywords_key.capitalize()
#
#     def find_metal(split_string):
#
#         """ Метод определяющий из какого металла изготовлено изделие.
#         Возвращает Название металла с пробой или None. """
#
#         if '585' in split_string or 'золото' in split_string:
#             return 'Золото 585'
#         elif '925' in split_string or 'серебро' in split_string:
#             return 'Серебро 925'
#
#     def find_weaving(split_string):
#
#         """ Метод определяющий плетения для цепей и браслетов, сопоставляет содержимое строки со списком вариантов.
#         Возвращает название плетения или None. """
#
#         for keywords_weaving_key, keywords_weaving_values in keywords_weaving.items():
#             for value in keywords_weaving_values:
#                 for elem in split_string:
#                     if value in elem:
#                         return keywords_weaving_key
#
#     def find_inserts(split_string):
#
#         """ Метод определяющий вставки в изделия, сопоставляет содержимое строки со списком вариантов.
#         Возвращает название плетения или None. """
#
#         for keywords_inserts_key, keywords_inserts_values in keywords_inserts.items():
#             for value in keywords_inserts_values:
#                 if value in split_string:
#                     return keywords_inserts_key
#
#     def find_size(split_string, group):
#
#         """ Метод определяющий размер изделия, перебирает елементы строки, проверяет их на причастность к числам и
#         сопоставляет с возможными вариантами размеров.
#          Возвращает вещественное число или None. """
#
#         if group == 'excel':
#             for _string in split_string:
#                 if _string.startswith('l-'):
#                     return _string[2:4] + '.0'
#
#         elif group == 'word':
#
#             index = (split_string.index('—') if '—' in split_string else split_string.index('---'))
#             right_part = ((' '.join(split_string).split(split_string[index])[1]).split(' '))[1:]
#
#             for el_r_part in right_part[-1::-1]:
#                 if len(el_r_part) > 1:
#                     if ',' in el_r_part:
#                         el_r_part.replace(',', '.')
#                     if isfloat(el_r_part):
#                         if el_r_part in sizes:
#                             return el_r_part
#                     if isinteger(el_r_part):
#                         if str(float(el_r_part)) in sizes:
#                             return str(float(el_r_part))
#
#     # Инструкция для функции "find_description"
#     if group == 'word':
#
#         arg = args[0]
#         description = f'{find_name(arg)}, {find_metal(arg)}'
#
#         # Определение вставок
#         inserts = find_inserts(arg)
#
#         # Определение размера для колец, цепей и браслетов
#         size = find_size(arg, group) if (description.split(' '))[0] in ('Кольцо', 'Цепь', 'Браслет') else None
#
#         # Определение плетения для цепей и браслетов
#         weaving = find_weaving(arg) if (description.split(' '))[0] in ['Цепь', 'Браслет'] else None
#
#         if inserts:
#             description = f'{description}, c {inserts}'
#
#         if weaving:
#             description = f'{description}, плетение - {weaving}'
#
#         if size:
#             description = f'{description}, {size} р-р'
#
#         return description
#
#     if group == 'excel':
#         _name = metal = weaving = size = inserts = None
#
#         for arg in args:
#             split_arg = str(arg).lower().split(' ')
#             if not _name:
#                 _name = find_name(split_arg)
#             if not metal:
#                 metal = find_metal(args[-1])
#             if not weaving:
#                 weaving = find_weaving(split_arg)
#             if not size:
#                 size = find_size(split_arg, group)
#             if not inserts:
#                 inserts = find_inserts(split_arg)
#
#         description = f'{_name}, {metal}'
#
#         if inserts:
#             description = f'{description}, c {inserts}'
#         if weaving:
#             description = f'{description}, плетение - {weaving}'
#         if size:
#             description = f'{description}, {size} р-р'
#
#         return description
#
