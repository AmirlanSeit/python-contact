# Импортируем библиотеки Tkinter, re и связанные с ней модули
from tkinter import *
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo, askyesno, showerror, INFO, OK
from tkinter import colorchooser
from tkinter import filedialog
import re
import json
import os

CONTACTS_FILE = "contacts.json"

# ===== Работа с JSON =====

def load_contacts():
    """Загружаем контакты из JSON или создаём дефолтные."""
    global contacts
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            contacts = json.load(f)
    else:
        # Дефолтные контакты
        contacts = {
            "Вася": {
                "phone": "+77015202702",
                "email": "afk@gmail.com",
                "image_path": "vasya.png"
            },
            "Петя": {
                "phone": "+77015202701",
                "email": "Petya@mail.ru",
                "image_path": "petya.png"
            },
            "Маша": {
                "phone": "+77015202720",
                "email": "qwerty@gmail.com",
                "image_path": "masha.png"
            },
        }
        save_contacts()


def save_contacts():
    """Сохраняем контакты в JSON."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)


# ===== Глобальные переменные для картинок и текущего контакта =====

contacts = {}
images = {}         # name -> PhotoImage
checks = []         # список RadioButton'ов
current_name = None # имя выбранного контакта
new_image_path = None  # путь к картинке при добавлении контакта


def get_image(name):
    """Ленивая загрузка картинки для контакта по имени."""
    global images
    path = contacts[name].get("image_path")
    if not path:
        return None
    if name not in images:
        try:
            images[name] = PhotoImage(file=path)
        except Exception:
            images[name] = None
    return images[name]


def build_contact_list():
    """Перестраиваем список RadioButton'ов с контактами."""
    global checks
    # Удаляем старые кнопки
    for btn in checks:
        btn.destroy()
    checks = []

    for idx, name in enumerate(contacts.keys()):
        def make_cmd(n=name):
            return lambda: select_contact(n)

        rb = Radiobutton(
            root,
            text=name,
            command=make_cmd(),
            value=idx,
            indicatoron=0,
            width=20,
            height=2
        )
        rb.grid(row=idx, column=0)
        checks.append(rb)


def select_contact(name):
    """Показать данные выбранного контакта в правой части окна."""
    global current_name
    current_name = name
    c = contacts[name]
    label.config(text=c.get("phone", ""))
    label1.config(text=c.get("email", ""))
    img = get_image(name)
    if img is not None:
        l1.config(image=img)
        l1.image = img
    else:
        l1.config(image="")
        l1.image = None


# ===== Функции интерфейса =====

# Функция для открытия файла и выбора картинки при добавлении контакта
def open_file():
    global new_image_path
    f_types = [('Png Files', '*.png'), ('Image Files', '*.png;*.jpg;*.jpeg;*.gif')]
    filepath = filedialog.askopenfilename(filetypes=f_types)
    if filepath:
        new_image_path = filepath


# Функция для выхода из программы
def exit123():
    exit(0)


# Функция для отображения информации о контактах
def qwerty():
    showinfo(
        title="Контактный телефон",
        message="Добро пожаловать на мой проект!",
        detail="Amirlan Seitkadyrov",
        icon=INFO,
        default=OK
    )


# Функция для открытия окна изменения контакта
def check():
    a = Toplevel()
    a['bg'] = 'green'
    root.iconbitmap(default="7269995.ico")
    a.geometry('270x170')
    Label(a, text="Имя:", bg='green').grid(row=0, column=0, sticky=W, pady=10, padx=10)
    table_name = Entry(a)
    table_name.grid(row=0, column=1, columnspan=3, sticky=W + E, padx=10)

    Label(a, text="Номер телефона:", bg='green').grid(row=1, column=0, sticky=W, pady=10, padx=10)
    table_phone = Entry(a)
    table_phone.grid(row=1, column=1, columnspan=3, sticky=W + E, padx=10)

    Label(a, text="Почта:", bg='green').grid(row=2, column=0, sticky=W, pady=10, padx=10)
    table_email = Entry(a)
    table_email.grid(row=2, column=1, columnspan=3, sticky=W + E, padx=10)

    def aboba():
        global contacts
        name = table_name.get()
        phone = table_phone.get()
        email = table_email.get()
        result = re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', phone)
        if bool(result):
            # сохраняем старую картинку, если контакт уже существовал
            old_image_path = contacts.get(name, {}).get("image_path")
            contacts[name] = {
                "phone": phone,
                "email": email,
                "image_path": old_image_path
            }
            save_contacts()
            build_contact_list()
            select_contact(name)
        else:
            mb.showerror("Ошибка", "Неправильно написан номер")

    Button(a, text='Изменить', command=aboba).grid(
        row=3, column=0, columnspan=4, sticky=W + E, padx=75, pady=10
    )


# Функция для открытия окна добавления нового контакта
def check1():
    a = Toplevel()
    a['bg'] = 'green'
    root.iconbitmap(default="7269995.ico")
    a.geometry('270x230')

    Label(a, text="Имя:", bg='green').grid(row=0, column=0, sticky=W, pady=10, padx=10)
    table_name = Entry(a)
    table_name.grid(row=0, column=1, columnspan=3, sticky=W + E, padx=10)

    Label(a, text="Номер телефона:", bg='green').grid(row=1, column=0, sticky=W, pady=10, padx=10)
    table_phone = Entry(a)
    table_phone.grid(row=1, column=1, columnspan=3, sticky=W + E, padx=10)

    Label(a, text="Почта:", bg='green').grid(row=2, column=0, sticky=W, pady=10, padx=10)
    table_email = Entry(a)
    table_email.grid(row=2, column=1, columnspan=3, sticky=W + E, padx=10)

    Label(a, text="Картинка:", bg='green').grid(row=3, column=0, sticky=W, pady=10, padx=10)
    button = Button(a, text="Открыть файл", command=open_file)
    button.grid(row=3, column=1, columnspan=3, sticky=W + E, padx=10)

    def aboba1():
        global contacts, new_image_path
        name = table_name.get()
        phone = table_phone.get()
        email = table_email.get()
        result = re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', phone)

        # проверяем уникальность номера и почты
        w = contacts.values()
        location = True
        for c in w:
            if phone == c.get("phone") or email == c.get("email"):
                location = False

        if len(contacts) <= 6 and bool(result) and name not in contacts and location:
            contacts[name] = {
                "phone": phone,
                "email": email,
                "image_path": new_image_path
            }
            save_contacts()
            build_contact_list()
            select_contact(name)
            new_image_path = None
        else:
            mb.showerror(
                "Ошибка",
                "Не хватает места или неправильно написан номер, "
                "или есть такой контакт/номер/почта"
            )

    Button(a, text='Добавить', command=aboba1).grid(
        row=4, column=0, columnspan=4, sticky=W + E, padx=75, pady=10
    )


# Функция для открытия окна удаления контакта
def check2():
    a = Toplevel()
    a['bg'] = 'green'
    root.iconbitmap(default="7269995.ico")
    a.geometry('210x90')

    Label(a, text="Имя:", bg='green').grid(row=0, column=0, sticky=W, pady=10, padx=10)
    table_name = Entry(a)
    table_name.grid(row=0, column=1, columnspan=3, sticky=W + E, padx=10)

    def aboba2():
        global contacts, current_name
        name = table_name.get()
        if name in contacts:
            # удаляем из словаря и из словаря картинок
            if name in images:
                del images[name]
            del contacts[name]
            save_contacts()
            build_contact_list()

            if current_name == name:
                current_name = None
                label.config(text='')
                label1.config(text='')
                l1.config(image='')
                l1.image = None

            showinfo("Результат", "Операция подтверждена")
        else:
            showerror(title="Результат", message="Нет такого контакта")

    Button(a, text='Удалить', command=aboba2).grid(
        row=1, column=0, columnspan=4, sticky=W + E, padx=75, pady=10
    )


# Функция для выбора цвета фона
def select_color():
    result = colorchooser.askcolor(initialcolor="black")
    color = result[1]
    if not color:
        return
    root["background"] = color
    label["background"] = color
    label1["background"] = color
    l1["background"] = color


# ===== Инициализация окна =====

root = Tk()
root.title("Contact")
root.iconbitmap(default="7269995.ico")

# Загружаем контакты из JSON или создаём дефолтные
load_contacts()

# Меню
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

# Виджеты справа (номер, почта, картинка)
label = Label(root, width=60, height=5)
label1 = Label(root, width=60, height=5)
l1 = Label(root, width=300, height=300)

label.place(x=200, y=0)
label1.place(x=200, y=50)
l1.place(x=250, y=150)

# Создаём список кнопок с контактами
build_contact_list()

root.geometry("1000x600")
root.mainloop()
