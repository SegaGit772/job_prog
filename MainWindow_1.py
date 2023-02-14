import tkinter
from tkinter import Tk, ttk, filedialog
from PrPclasses import PrP
from Tubes_classes_27_01 import Create_Tube
from Kclasses import Create_kalitka
from GateClasses import Create_gate
from datetime import datetime


"""Класс создаст окно где изменю данные выбранной строки"""


class Change_row(tkinter.Toplevel):
    def __init__(self, my_dict):
        self.text_got = my_dict[0]
        self.amount_got = my_dict[1]
        self.summa_got = my_dict[2]

        super().__init__()
        self.text = tkinter.Entry(self, width=8)
        self.text.pack()
        self.text.insert(0, "{}".format(self.text_got))
        self.amount = tkinter.Entry(self, width=8)
        self.amount.pack()
        self.amount.insert(0, "{}".format(self.amount_got))
        self.summa = tkinter.Entry(self, width=8)
        self.summa.pack()
        self.summa.insert(0, "{}".format(self.summa_got))
        self.destr_but = tkinter.Button(self, text="Закрыть", command=self.window_destr)
        self.destr_but.pack()

    def open(self):
        self.grab_set()
        self.wait_window()
        return lst

    def window_destr(self):
        global lst
        lst = [self.text.get(), self.amount.get(), self.summa.get()]
        Change_row.destroy(self)


class Main(Tk):
    def __init__(self):
        super().__init__()
        self.i = len(c)
        self.tree = ttk.Treeview(columns=title, height=self.i, show="headings")
        self.tree.heading("1", text="Описание")
        self.tree.heading("2", text="Кол-во")
        self.tree.heading("3", text="Стоимость")
        self.tree.column('1', minwidth=220, width=400, stretch=True)
        self.tree.column('2', minwidth=70, width=70)
        self.tree.column('3', minwidth=70, width=70, )
        self.tree.grid(column=0, row=0, columnspan=6)

        self.addPrP = ttk.Button(self, text='ПрП', command=self.start_prp, width=11)
        self.addPrP.grid(column=0, row=1)
        self.addTubes = ttk.Button(self, text='Трубы', command=self.start_tubes)
        self.addTubes.grid(column=1, row=1)
        self.addKalitka = ttk.Button(self, text="Калитка", command=self.start_kalitka)
        self.addKalitka.grid(column=2, row=1)
        self.addvr = ttk.Button(self, text="Ворота Р", command=self.start_vr)
        self.addvr.grid(column=3, row=1)

        self.del_but = ttk.Button(self, text="Удалить", command=self.del_func).grid(column=4, row=1)
        self.sum_but = ttk.Button(self, text="Сумма", command=self.sum_func).grid(column=5, row=1)
        self.sum_labl = ttk.Label(self, text="")
        self.sum_labl.grid(column=5, row=2)
        self.save_but = ttk.Button(self, text="Сохранить", width=11, command=self.create_data)
        self.save_but.grid(column=0, row=2)
        self.load_but = ttk.Button(self, text="Открыть", command=self.open_data)
        self.load_but.grid(column=1, row=2)
        self.change_amount = ttk.Button(self, text="Изменить", width=11, command=self.change_am)  # изменить строку
        self.change_amount.grid(column=2, row=2)

    def change_am(self):
        get_dict = self.tree.focus()
        my_dict = self.tree.item(get_dict)
        a = Change_row(my_dict["values"])
        b = a.open()
        self.tree.delete(get_dict)
        self.tree.insert("", "end", values=b)
        self.tree.config(height=len(self.tree.get_children()))

    """нажимая кнопку сохранить я вызываю функцию, которая создаст переменную data, где будет храниться инфа
     для сохранения. А эта Ф после выполнения  вызывет Ф save_data(data) которая и сохранит в файл информацию.
    """
    def create_data(self):
        data = ""
        for k in self.tree.get_children(""):
            text = str(self.tree.set(k, 1))
            amount = str(self.tree.set(k, 2))
            price = str(self.tree.set(k, 3))
            data_add = (text + ";" + amount + ";" + price + "\n")
            data += data_add
        self.save_data(data)

    """Сохраняем расчеты в файл"""
    def save_data(self, data):
        filepath = filedialog.asksaveasfilename(initialdir="saves")
        if filepath != "":
            with open(filepath, "w") as file:
                file.write(data)

    """По кнопке Открыть загружаем дату из saves"""
    def open_data(self):
        filepath = filedialog.askopenfilename(initialdir="saves")
        if filepath != "":
            with open(filepath) as file:
                data = file.readlines()  # считывает из файлы все строки в список и возвращает его
        self.put_data(data)

    """Передаем загруженную дату в Ф, которая заполнит таблицу начального экрана"""
    def put_data(self, data):
        for info in data:
            text, amount, price = info.rstrip("\n").split(";")
            data_insert = [text, amount, price]
            self.tree.insert('', 'end', values=data_insert)
            self.tree.config(height=len(self.tree.get_children()))

    """Ф считает сумму всех строк в таблице последовательным извлечением строк, перемножением кол-ва на сумму, 
    добавлением всего в список. Пробежав по всей таблице суммирует ее и выводит в лейбле"""
    def sum_func(self):
        i = []
        for k in self.tree.get_children(""):
            amount = int(self.tree.set(k, 2))
            summa = int(self.tree.set(k, 3))
            amount_summa = amount * summa
            i.append(amount_summa)
        self.sum_labl.configure(text=f"{sum(i)}")
        # print(self.tree.item(k))  вернет целую строку
        # print(k) # I001
        # print(self.tree.item(k)) {'text': '', 'image': '', 'values': ['ПрП В/Ш 300x3000 яч.150x150 D=12', 1, 1296], 'open': 0, 'tags': ''}

    """Удаление выбранной строки"""
    def del_func(self):
        item = self.tree.selection()[0]
        self.tree.delete(item)
        self.sum_func()

    def start_prp(self):
        prpwin = PrP()
        prp = prpwin.open()
        text = f"""ПрП В/Ш {prp[0]}x{prp[1]} яч.{prp[2]}x{prp[3]} D={prp[4]}"""
        people = [text, prp[5], prp[6]]
        self.tree.insert('', "end", values=people)
        self.tree.config(height=len(self.tree.get_children()))

    """Ф вызова окна расчета труб и передача результата в главное окно. Важно учесть что в Ф return нельзя передать
    Ф типа width_1.get()"""
    def start_tubes(self):
        tubes = Create_Tube()
        tbs = tubes.open()

        text = f"""Опоры: {tbs["combo_w_1"]}: {tbs["width1_1"]}x{tbs["width1_2"]}x{tbs["thick1"]};
        {tbs["combo_w_2"]}: {tbs["width2_1"]}x{tbs["width2_2"]}x{tbs["thick2"]}. Фланец {tbs["flanec"]},
        {tbs["kosynka"]}
        """
        result = [text, "12", "12"]
        self.tree.insert('', "end", values=result)
        self.tree.config(height=len(self.tree.get_children()))

    def start_kalitka(self):
        a = Create_kalitka()
        text, summa = a.open()
        result = [text, 1, summa]
        self.tree.insert("", "end", values=result)
        self.tree.config(height=len(self.tree.get_children()))

    def start_vr(self):
        a = Create_gate()
        text, summa = a.open()
        result = [text, 1, summa]
        self.tree.insert("", "end", values=result)
        self.tree.config(height=len(self.tree.get_children()))

if __name__ == "__main__":
    c = []
    title = ('1', "2", "3")
    b = datetime.date(datetime.now())
    g = "09/05/2023"
    e = datetime.strptime(g, "%d/%m/%Y")
    time_now = datetime.now()
    if e < time_now:
       raise Exception("Some exception")
    root = Main()
    root.mainloop()


"""
https://metanit.com/python/tkinter/4.1.php - работа с таблицами
https://metanit.com/python/tkinter/5.3.php - сохр/откр файла
https://www.piknad.ru/pytab3.php - редактор ячеек TreeView
"""
"""
1. ЧТобы получить словарь данных из выбранного мной на экране:
a = self.tree.focus()
print(self.tree.item(a)
"""
