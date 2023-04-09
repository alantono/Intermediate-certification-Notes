from pathlib import Path


def list_view():
    d = Path('Notebook.txt')
    with open(d, 'r', encoding="utf-8") as data:
        return data.read()
    

def write_data_1(notes_list):
    d = Path('Nb.txt')
    with open(d, 'w', encoding="utf-8") as data:
        for listitem in notes_list:
            data.writelines('%s\n' % listitem)

def read_data_1():
    notes_list = []
    d = Path('Nb.txt')
    with open(d, 'r', encoding="utf-8") as data:
        for line in data:
            currentPlace = line[:-1]
            notes_list.append(currentPlace)
        return notes_list

def write_data(notes_list):
    d = Path('Notebook.txt')
    with open(d, 'w', encoding="utf-8") as data:
        for i in range(0, int(len(notes_list))):
            a = f"{notes_list[i]};\n"
            data.writelines(a)

def write_data1(id, header, text, data): # использовалась для редактирования
    d = Path('Notebook.txt')
    with open(d, 'a', encoding="utf-8") as data:
        a = f"{id}{header}{text}{data}\n"
        data.write(a)

def write_read_csv():  # запись в csv файл
    import csv
    # получаем список строк из файла Notebook.txt
    a = list(list_view().split())
    z = len(a)
    with open('Notebook.csv', 'w', newline='', encoding="utf-8") as data:
        csvwriter = csv.writer(data)
        # добавляем названия столбцов
        csvwriter.writerow(['id'] + ['Заголовок'] + ['Заметка'] + ['Дата'])
        while z != 0:
            csvwriter.writerow([a[0], a[1], a[2], a[3]])  # построчная запись
            del a[:4]
            z = z - 4
    with open('Notebook.csv', 'r', newline='', encoding="utf-8") as data:  # читаем csv файл
        csvreader = csv.reader(data)
        for row in csvreader:
            print(' '.join(row))  # и выводим на экран csv файл
