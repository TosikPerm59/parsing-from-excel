import docx
import os


def check_outgoing_invoice(invoice_path):
    if not invoice_path.endswith('.docx'):
        return
    document = docx.Document(invoice_path)
    sender = 'ИП Александрова Елена Петровна "Golden_Sun", ИНН: 591792868890, улица Уральская дом 1'

    if 'Унифицированная форма № ТОРГ-12' in document.paragraphs[0].text:
        if len(document.paragraphs) == 3:
            return True


def check_file_path(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            return True


def check_id(_id):
    if not _id:
        return
    if len(_id) > 13 and _id[-1] == ' ':
        _id = _id[: -1]
    if len(_id) == 13 and _id.isdigit():
        return _id
    if _id == '0':
        return _id
    else:
        return
