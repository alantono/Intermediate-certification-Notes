
from tkinter.scrolledtext import ScrolledText
import functions
import logger
from tkinter import *
from tkinter import font

def button_click():
    logger.log("Программа запущена")

root = Tk()
root.title("Заметки")
root.geometry("820x300+400+400")
root.resizable(width=False, height=False)

def clear_entry(): # очистка полей: имя фамилия телефон
        header.delete(0, END)
        note_text.delete(1.0, END)
        time.delete(0, END)

def mistake_entry(): # ошибочный ввод данных
        mistake_entry = Tk()
        mistake_entry.title("Сообщение")
        mistake_entry.geometry("300x30+1200+400")
        label = Label(mistake_entry, text="Такой заметки нет!", font=("Arial", 12))
        label.pack()
        clear_entry()
        mistake_entry.mainloop()

def mistake_entry_1(): # не заполнено поле Заглавие и текст
        mistake_entry = Tk()
        mistake_entry.title("Сообщение")
        mistake_entry.geometry("300x30+1200+400")
        label = Label(mistake_entry, text="Введите заглавие заметки и текст", font=("Arial", 12))
        label.pack()
        mistake_entry.mainloop()

def mistake_entry_data(): # ошибочный ввод даты
        mistake_entry = Tk()
        mistake_entry.title("Сообщение")
        mistake_entry.geometry("300x90+1200+400")
        label = Label(mistake_entry, text="На данную дату Заметок нет \nили Введена некорректная дата.\nВведите дату в формате 2023.03.15", font=("Arial", 11))
        label.pack()
        clear_entry()
        mistake_entry.mainloop()

def enter1(event):# вывод в отдельном окне Списка абонентов
        window_text = Tk()
        window_text.title("Список заметок")
        window_text.geometry("350x400+1400+400")
        t = Text(window_text)
        t.pack()
        t.insert(1.0, functions.func_1())
        window_text.mainloop()

def enter2(event): # Добавление новой Заметки
        functions.func_2()
        add_note = Tk() # вывод в отдельном окне добавленной заметки
        add_note.title("Заметка сохранена")
        add_note.geometry("200x200+1200+400")
        label_aa = Label(add_note, text="", font=("Arial", 12), justify=LEFT)
        label_aa["text"] = functions.func_2_1()
        label_aa.pack()
        clear_entry()
        add_note.mainloop()

def enter3(event): # Удаление заметки
        functions.func_3()
        del_note = Tk() # вывод в отдельном окне удаленного абонента
        del_note.title("Заметка удалена")
        del_note.geometry("400x200+1200+400")
        label_da = Label(del_note, text="", font=("Arial", 12), justify=LEFT)
        label_da["text"] = functions.func_3_1()
        label_da.pack()
        clear_entry()
        del_note.mainloop()
      

def enter4(event): # редактирование абонента. кнопка Редактировать
        functions.func_4()
   

def enter4_1(event): # редактирование абонента. кнопка Ок
        functions.func_4_1()
        add_note = Tk() # вывод в отдельном окне добавленной заметки
        add_note.title("Заметка отредактирована")
        add_note.geometry("300x200+1200+400")
        label_aa = Label(add_note, text="", font=("Arial", 12), justify=LEFT)
        label_aa["text"] = functions.func_4_2()
        label_aa.pack()
        clear_entry()
        add_note.mainloop()

def enter5(event): # Вывод в отдельном окне список заметок на указанную дату
        functions.func_5()
        window_text = Tk()
        window_text.title("Список заметок")
        window_text.geometry("300x500+1400+400")
        t = Text(window_text)
        t.pack()
        t.insert(1.0, functions.func_5())
        clear_entry()
        window_text.mainloop()

def enter6(event):
        functions.func_6()

def enter7(event): # во избежание нажатия клавиши Enter в поле Text (при нажатии Enter при редактировании текста заметки строка разбивается на список)
        mistake_entry = Tk()
        mistake_entry.title("Сообщение")
        mistake_entry.geometry("300x90+1200+400")
        label = Label(mistake_entry, text="Нажатие Enter неприменимо.\nДля сохранения изменений\nНажмите кнопку Сохранить изменения", font=("Arial", 12))
        label.pack()
        mistake_entry.mainloop()

l2 = Label(root, text='Создать заметку. Заполните Заголовок и Текст заметки и нажмите "Добавить"', font=("Arial", 10)).place(x = 210, y = 10)
l3 = Label(root, text='Удалить заметку. Введите Заголовок заметки и нажмите "Удалить"', font=("Arial", 10)).place(x = 210, y = 40)
l4 = Label(root, text='Редактировать заметку. Введите Заголовок заметки и нажмите "Редактировать"', font=("Arial", 10)).place(x = 210, y = 70)
l5 = Label(root, text='Показать Заметки на указанную дату.', font=("Arial", 10)).place(x = 210, y = 160)
l5_2 = Label(root, text='Введите дату в формате гггг.мм.дд:', font=("Arial", 10)).place(x = 210, y = 190)
l5_3 = Label(root, text=' и нажмите "Показать"', font=("Arial", 10)).place(x = 540, y = 190)

b1 = Button(root, text="Просмотр всех заметок", width=25, height=1)
b2 = Button(root, text="Добавить", width=13, height=1)
b3 = Button(root, text="Удалить", width=13, height=1)
b4 = Button(root, text="Редактировать", width=13, height=1)
b4_1 = Button(root, text="Сохранить изменения", width=19, height=1)
b5 = Button(root, text="Показать", width=13, height=1)
b6 = Button(root, text="Экспорт заметок в csv файл", width=25, height=1)

l_surname = Label(root, text='Заголовок', font=("Arial Black", 10)).place(x = 10, y = 10)
l_name = Label(root, text='После редактирования заметки нажмите "Сохранить изменения"', font=("Arial", 10)).place(x = 210, y = 100)
l_ph_number = Label(root, text='Текст заметки', font=("Arial Black", 10)).place(x = 10, y = 70)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar() 
v5 = StringVar()

header = Entry(root, textvariable=v1, width=21, justify=LEFT,
        font=font.Font(family="Arial Black", size=10)) # поле для ввода Заголовка
header.place(x=10, y=40)
note_text = Text(root, width=26, height=10, 
        font=font.Font(family="Arial", size=10), wrap=WORD) # поле для ввода текста заметки
note_text.place(x = 10, y = 100)
time = Entry(root, textvariable=v4, width= 12, justify=LEFT,
        font=font.Font(family="Arial Black", size=10))
time.place(x = 430, y = 190)

b1.bind('<Button-1>', enter1)
b1.place(x = 210, y = 230)
b2.bind('<Button-1>', enter2)
b2.place(x = 700, y = 10)
b3.bind('<Button-1>', enter3)
b3.place(x = 700, y = 40)
b4.bind('<Button-1>', enter4)
b4.place(x = 700, y = 70)
b4_1.bind('<Button-1>', enter4_1)
b4_1.place(x = 660, y = 100)
b5.bind('<Button-1>', enter5)
b5.place(x = 700, y = 190)
b6.bind('<Button-1>', enter6)
b6.place(x = 210, y = 260)

note_text.bind('<Return>', enter7) # нажатие клавиши Enter

root.mainloop()
logger.log("Программа закрыта")