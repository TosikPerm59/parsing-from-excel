import docx
import os


def check_invoice(invoice_path):
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
    return len(_id) == 13 and _id.isdigit()
