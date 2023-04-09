from data_base import write_data_1, list_view, write_data, write_data1, write_read_csv, read_data_1
import controller
from pathlib import Path
import logger
from tkinter import *
import datetime


notes_list = []
def func_1():                                                   # Вывод всех Заметок в отдельном окне
    logger.log("Просмотрены все заметки")
    a = list_view()
    return a

def func_2():                                                    # Добавление новой Заметки
    notes_list = read_data_1()                                   # считываем последнюю редакцию списка заметок
    today = datetime.datetime.today()
    notes_list.append(str(int(len(notes_list) / 4)+1))           # добавили в список id
    notes_list.append(controller.v1.get())                       # добавили в список Заголовок
    notes_list.append(controller.note_text.get(1.0, END))        # добавили в список Текст заметки
    notes_list[-1] = notes_list[-1].strip()                      # убрали из списка \n перенос строки после Текста заметки
    notes_list.append(str(today.strftime("%Y.%m.%d")))           # добавили в список дату и время заметки
    logger.log('Добавлена заметка: {}'.format(notes_list))
    write_data_1(notes_list)                                     # записали список в файл Notebook.txt (для вывода списка заметок)
    write_data(notes_list)                                       # записали список в файл Nb.txt (для сохранения списка)
    return notes_list

def func_2_1():                                                  # Вывод добавленной заметки на экран
    today = datetime.datetime.today()
    b = str(today.strftime("%Y.%m.%d"))
    a = f"Добавлена заметка №: {str(int(len(notes_list) / 4)+1)} \n\nДата: {b}\n\nЗаголовок: {controller.v1.get()} \n\nТекст: \n{controller.note_text.get(1.0, END)}"
    return a

def func_3():                                                       # Удаление записи тел книги по фамилии или имени
    global x
    x = str("")
    del_rec = controller.v1.get()                                   # присваивем переменной del_rec - Заголовок удаляемой заметки
    logger.log('Пользователь сделал запрос на удаление: {}'.format(del_rec))
    notes_list = read_data_1()                                      # считываем последнюю редакцию списка заметок
    if del_rec not in notes_list:
        controller.mistake_entry()                                  # вызывает сообщение о том что Заметки нет в списке
    else:
        index = notes_list.index(del_rec)                           # получаем индекс Заголовока удаляемой заметки
        logger.log('Удалена заметка:{} {} {} {}'.format(
                notes_list[index - 1], notes_list[index], notes_list[index + 1], notes_list[index + 2]))
        x = f"Удалена заметка №: {str(notes_list[index - 1])} \n\nДата: {notes_list[index + 2]}\n\nЗаголовок: {notes_list[index]} \n\nТекст: \n{notes_list[index + 1]}"   
        del notes_list[index + 2]                                   # удалили из списка дату и время заметки
        del notes_list[index + 1]                                   # удалили из списка Текст заметки
        del notes_list[index]                                       # удалили из списка Заголовок заметки
        del notes_list[index - 1]                                   # удалили из списка id заметки
        for j in range(index - 1, len(notes_list), 4):              # обновляем id каждой Заметки после удаленной заметки
            notes_list[j] = str(int(notes_list[j]) - 1)
        write_data_1(notes_list)                                    # после удаления Заметки записали обновленный список в файл Notebook.txt (для вывода списка заметок)
        write_data(notes_list)                                      # после удаления Заметки записали обновленный список в файл Nb.txt (для сохранения списка)

def func_3_1():                                                     # Вывод удаленной заметки в отдельном окне
    return x

def func_4():                                                       # Редактирование записи в тел книге (кнопка Редактировать)
    ed_rec = controller.v1.get()                                    # присваивем переменной ed_rec - Заголовок удаляемой заметки
    logger.log('Пользователь сделал запрос на редактирование заметки: {}'.format(ed_rec))
    notes_list = read_data_1()                                      # считываем последнюю редакцию списка заметок
    if ed_rec not in notes_list:
        controller.mistake_entry()                                  # вызывает сообщение о том что Заметки нет в списке
    else:
        index = notes_list.index(ed_rec)                            # получаем индекс Заголовока удаляемой заметки
        controller.note_text.insert("1.0", str(notes_list[index+1]) ) # открываем текст заметки в поле Текст для редактирования
    return str(notes_list[index+1])    

def func_4_1(): # Редактирование записи в тел книге (кнопка Сохранить изменения).
    notes_list = read_data_1() # считываем из файла Nb.txt последнюю редакцию списка заметок
    index = notes_list.index(controller.v1.get()) # получаем индекс Заголовока редактируемой заметки
    notes_list[index + 1] = controller.note_text.get(1.0, END) # добавили в список Текст отредактированной заметки
    logger.log('Отредактирована заметка:{} {} {} {}'.format(
                notes_list[index - 1], notes_list[index], notes_list[index + 1], notes_list[index + 2]))
    write_data_1(notes_list)  # записали список в файл Notebook.txt (для вывода списка заметок)
    write_data(notes_list)    # записали список в файл Nb.txt (для сохранения списка)
    return notes_list

def func_4_2():  # Вывод отредактированной заметки в отдельном окне
    today = datetime.datetime.today()
    b = str(today.strftime("%Y.%m.%d"))
    a = f"Отредактирована заметка №: {str(int(len(notes_list) / 4)+1)} \n\nДата: {b}\n\nЗаголовок: {controller.v1.get()} \n\nТекст: \n{controller.note_text.get(1.0, END)}"
    return a   
    
def func_5():  # Поиск Заметки по дате (кнопка показать)
    logger.log('Пользователь сделал запрос на поиск заметок на дату: {}'.format(controller.v4.get()))
    list = []
    notes_list = read_data_1() # считываем из файла Nb.txt последнюю редакцию списка заметок
    if controller.v4.get() not in notes_list:
        controller.mistake_entry_data()  # вызывает сообщение о том что введенной даты нет в списке
    else:
        a = f"Список Заметок от {controller.v4.get()}  \n\n"
        list.append(a)
        for i in range(3, len(notes_list), 4):
            if notes_list[i] == controller.v4.get():
                    a = f"Заметка №: {notes_list[i - 3]} \n\nЗаголовок: {notes_list[i - 2]} \n\nТекст: \n{notes_list[i - 1]}"
                    list.append(a)
    return list

def func_6():  # Экспорт заметок в csv файл
    write_read_csv()
    logger.log("Заметки экспортированы в csv файл")

