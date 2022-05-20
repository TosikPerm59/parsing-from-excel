import os


def directory_parsing(path_to_invoices):
    filelist = []

    for file in os.listdir(path_to_invoices):
        if file.endswith('.docx'):
            filelist.append()

    return filelist

directory_parsing("E:\Elena\Desktop\Документы  Александрова Е.П\Накладные Кирпичникова Маргарита")