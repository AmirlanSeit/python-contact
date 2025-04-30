# Импортируем библиотеки Tkinter, re и связанные с ней модули
from tkinter import *
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo, askyesno, showerror, INFO, OK
from tkinter import colorchooser
from tkinter import filedialog
import re


# Функция для открытия файла и загрузки изображения
def open_file():
    global img4
    f_types = [('Png Files', '*.png')]
    filepath = filedialog.askopenfilename(filetypes=f_types)
    img4 = PhotoImage(file=filepath)


# Функция для выхода из программы
def exit123():
    exit(0)


# Функция для отображения информации о контактах
def qwerty():
    showinfo(title="Контактный телефон", message="Добро пожаловать на мой проект!", detail="Amirlan Seitkadyrov",
             icon=INFO, default=OK)


# Функция для открытия окна изменения контакта
def check():
    a = Toplevel()
    a['bg'] = 'green'
    root.iconbitmap(default="7269995.ico")
    a.geometry('270x170')
    labelq = Label(a, text="Номер телефона:", bg='green').grid(row=1, column=0, sticky=W, pady=10, padx=10)
    table_number = Entry(a)
    table_number.grid(row=1, column=1, columnspan=3, sticky=W + E, padx=10)
    labelq1 = Label(a, text="Имя:", bg='green').grid(row=0, column=0, sticky=W, pady=10, padx=10)
    table_number1 = Entry(a)
    table_number1.grid(row=0, column=1, columnspan=3, sticky=W + E, padx=10)
    labelq2 = Label(a, text="Почта:", bg='green').grid(row=2, column=0, sticky=W, pady=10, padx=10)
    table_number2 = Entry(a)
    table_number2.grid(row=2, column=1, columnspan=3, sticky=W + E, padx=10)

    # Вложенная функция для обработки изменения контакта
    def aboba():
        e = table_number1.get()
        r = table_number.get()
        g = table_number2.get()
        result = re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', r)
        if bool(result) is True:
            sp[e] = [r, g]
        else:
            mb.showerror("Ошибка", "Неправильно написан номер")

    butq = Button(a, text='Изменить', command=aboba).grid(row=3, column=0, columnspan=4, sticky=W + E, padx=75, pady=10)


# Функция для открытия окна добавления нового контакта
def check1():
    a = Toplevel()
    a['bg'] = 'green'
    root.iconbitmap(default="7269995.ico")
    a.geometry('270x200')
    labelq = Label(a, text="Номер телефона:", bg='green').grid(row=1, column=0, sticky=W, pady=10, padx=10)
    table_number = Entry(a)
    table_number.grid(row=1, column=1, columnspan=3, sticky=W + E, padx=10)
    labelq1 = Label(a, text="Имя:", bg='green').grid(row=0, column=0, sticky=W, pady=10, padx=10)
    table_number1 = Entry(a)
    table_number1.grid(row=0, column=1, columnspan=3, sticky=W + E, padx=10)
    labelq2 = Label(a, text="Почта:", bg='green').grid(row=2, column=0, sticky=W, pady=10, padx=10)
    table_number2 = Entry(a)
    table_number2.grid(row=2, column=1, columnspan=3, sticky=W + E, padx=10)
    labelq3 = Label(a, text="Картинка:", bg='green').grid(row=3, column=0, sticky=W, pady=10, padx=10)

    button = Button(a, text="Открыть файл", command=open_file)
    button.grid(row=3, column=1, columnspan=3, sticky=W + E, padx=10)

    # Вложенная функция для обработки добавления нового контакта
    def aboba1():
        e = table_number1.get()
        r = table_number.get()
        g = table_number2.get()
        number = r
        result = re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', number)
        w = sp.values()
        location = True
        for i in w:
            if r in i or g in i or img4 in i:
                location = False
        if len(sp) <= 6 and bool(result) is True and e not in sp and location is True:
            x = len(sp)
            sp[e] = [r, g, img4]

            # Вложенная функция для изменения выбранного контакта
            def change3():
                label.config(text=sp[str(e)][0])
                label1.config(text=sp[str(e)][1])
                l1.config(image=img4)

            b4 = Radiobutton(root, text=e, command=change3, value=x, indicatoron=0, width=20, height=2)
            x += 1
            b4.grid(row=len(sp) + 1, column=0)
            checks.append(b4)
        else:
            mb.showerror("Ошибка", "Не хватает места или неправильно написан номер или есть такой контакт")

    butq = Button(a, text='Добавить', command=aboba1).grid(row=4, column=0, columnspan=4, sticky=W + E, padx=75,
                                                           pady=10)


# Функция для открытия окна удаления контакта
def check2():
    a = Toplevel()
    a['bg'] = 'green'
    root.iconbitmap(default="7269995.ico")
    a.geometry('210x90')
    labelq1 = Label(a, text="Имя:", bg='green').grid(row=0, column=0, sticky=W, pady=10, padx=10)
    table_number1 = Entry(a)
    table_number1.grid(row=0, column=1, columnspan=3, sticky=W + E, padx=10)

    # Вложенная функция для обработки удаления контакта
    def aboba2():
        name = table_number1.get()
        if name in sp.keys():
            number = label['text']
            keys = list(sp.keys())
            for i in range(len(keys)):
                if keys[i] == name:
                    index = i
            checks[index].destroy()
            del checks[index]
            del sp[name]
            loc = False
            w = sp.values()
            print(number)
            for q in w:
                if number in q:
                    loc = True
            if loc is False:
                label.config(text='')
                label1.config(text='')
                l1.config(image='')
            showinfo("Результат", "Операция подтверждена")
        else:
            showerror(title="Результат", message="Нету такого контакта")

    butq = Button(a, text='Удалить', command=aboba2).grid(row=1, column=0, columnspan=4, sticky=W + E, padx=75, pady=10)


# Функция для выбора цвета фона
def select_color():
    result = colorchooser.askcolor(initialcolor="black")
    root["background"] = result[1]
    label["background"] = result[1]
    label1["background"] = result[1]
    l1["background"] = result[1]




root = Tk()
root.title("Contact")
root.iconbitmap(default="7269995.ico")
img3 = PhotoImage(file="masha.png")
img2 = PhotoImage(file="petya.png")
img1 = PhotoImage(file="vasya.png")
sp = {'Вася': ['+77015202702', 'afk@gmail.com', img1],
      'Петя': ['+77015202701', 'Petya@mail.ru', img2],
      'Маша': ['+77015202720', 'qwerty@gmail.com', img3]}


# Функции для изменения информации о контактах
def change():
    label.config(text=sp['Вася'][0])
    label1.config(text=sp['Вася'][1])
    l1.config(image=img1)


def change1():
    label.config(text=sp['Петя'][0])
    label1.config(text=sp['Петя'][1])
    l1.config(image=img2)


def change2():
    label.config(text=sp['Маша'][0])
    label1.config(text=sp['Маша'][1])
    l1.config(image=img3)


mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu1 = Menu(mainmenu, tearoff=0)
filemenu1.add_command(label="INFO", command=qwerty)
filemenu1.add_command(label="Изменить фон", command=select_color)
filemenu1.add_separator()
filemenu1.add_command(label="Exit", command=exit123)
mainmenu.add_cascade(label='Справка', menu=filemenu1)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Изменить", command=check)
filemenu.add_command(label="Добавить", command=check1)
filemenu.add_command(label="Удалить", command=check2)
mainmenu.add_cascade(label="Файл", menu=filemenu)

b1 = Radiobutton(root, text="Вася", command=change, value=0, indicatoron=0, width=20, height=2)
b2 = Radiobutton(root, text="Петя", command=change1, value=1, indicatoron=0, width=20, height=2)
b3 = Radiobutton(root, text="Маша", command=change2, value=2, indicatoron=0, width=20, height=2)
checks = [b1, b2, b3]
images = [img1, img2, img3]
label = Label(root, width=60, height=5)
label1 = Label(root, width=60, height=5)
l1 = Label(root, width=300, height=300)
b1.grid(row=0, column=0)
b2.grid(row=1, column=0)
b3.grid(row=2, column=0)
label.place(x=200, y=0)
label1.place(x=200, y=50)
l1.place(x=250, y=150)
root.geometry("1000x600")
root.mainloop()
