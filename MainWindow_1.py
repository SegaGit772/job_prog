from tkinter import Tk, ttk, filedialog
from PrPclasses import PrP
from Tubes_classes_27_01 import Create_Tube
from Kclasses import Create_kalitka

class Main(Tk):
    def __init__(self):
        super().__init__()
        self.i = len(c)
        self.tree = ttk.Treeview(columns=title, height=self.i,
                                 show="headings")
        self.tree.heading('1', text="Описание")
        self.tree.heading("2", text="Кол-во")
        self.tree.heading("3", text="Стоимость")
        self.tree.column('1', minwidth=220, width=300, stretch=True)
        self.tree.column('2', minwidth=70, width=70)
        self.tree.column('3', minwidth=70, width=70, )
        self.tree.grid(column=0, row=0, columnspan=6)

        self.addPrP = ttk.Button(self, text='ПрП', command=self.start_prp, width=11)
        self.addPrP.grid(column=0, row=1)
        self.addTubes = ttk.Button(self, text='Трубы', command=self.start_tubes)
        self.addTubes.grid(column=1, row=1)
        self.addKalitka = ttk.Button(self, text="Калитка", command=self.start_kalitka)
        self.addKalitka.grid(column=2, row=1)
        self.del_but = ttk.Button(self, text="Удалить", command=self.del_func).grid(column=3, row=1)
        self.sum_but = ttk.Button(self, text="Сумма", command=self.sum_func).grid(column=4, row=1)
        # self.sum_labl_labl = ttk.Button(self, text="Сумма").grid(column=3, row=1)
        self.sum_labl = ttk.Label(self, text="")
        self.sum_labl.grid(column=4, row=2)
        self.save_but = ttk.Button(self, text="Сохранить", width=11, command=self.create_data)
        self.save_but.grid(column=0, row=2)
        self.load_but = ttk.Button(self, text="Открыть", command=self.open_data)
        self.load_but.grid(column=1, row=2)

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


        """    def func(self, *items):
        for j in items:
            self.tree.insert('', ttk.END, values=(j,))
        self.tree.config(height=len(self.tree.get_children()))"""

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
        people = [text, "12", "12"]
        self.tree.insert('', "end", values=people)
        self.tree.config(height=len(self.tree.get_children()))
        """results = {"combo_w_1": combo_w_1, "width1_1": width1_1, "width1_2": width1_2, "thick1": thickness1,
                   "flanec": flanec_name, "kosynka": kosynka_name,
                   "combo_w_2": combo_w_2, "width2_1": width2_1, "width2_2": width2_2, "thick2": thickness2}"""



    def start_kalitka(self):
        a = Create_kalitka()


if __name__ == "__main__":
    c = []
    title = ('1', "2", "3")
    root = Main()
    root.mainloop()

"""
https://metanit.com/python/tkinter/4.1.php - работа с таблицами
https://metanit.com/python/tkinter/5.3.php - сохр/откр файла

"""

