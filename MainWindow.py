from tkinter import *
from tkinter import ttk
from PrPclasses import PrP
from Tubes_classes_27_01 import Create_Tube
from Kclasses import Create_kalitka

def add():
    ...


class App(Tk):
    columns = ('name', 'amount', 'cost')

    def __init__(self):
        super().__init__()
        self.addPrP = Button(self, text='ПрП', command=self.start_prp, width=5)
        self.addPrP.grid(column=1, row=0)
        self.addTubes = Button(self, text='Трубы', command=self.start_tubes)
        self.addTubes.grid(column=1, row=1)  # или в меню файл хранить добавление ячеек
        self.addKalitka = Button(self, text="Калитка", command=self.start_kalitka)
        self.addKalitka.grid(column=1, row=2)
        self.del_but = Button(self, text="Удалить", command=self.del_func).grid(column=1, row=3)

        self.tree = ttk.Treeview(self, columns=App.columns, show='headings')
        self.tree.grid(column=0, row=0, columnspan=4)
        self.tree.heading('name', text='Описание', )
        self.tree.heading('amount', text='Кол-во')
        self.tree.heading('cost', text='Стоимость')
        self.tree.column('name', minwidth=220, width=220)
        self.tree.column('amount', minwidth=70, width=70)
        self.tree.column('cost', minwidth=70, width=70)

    def del_func(self):
        item = self.tree.selection()[0]
        self.tree.delete(item)

    def start_prp(self):
        prpwin = PrP()
        prp = prpwin.open()
        text = f"""ПрП В/Ш {prp[0]}x{prp[1]} яч.{prp[2]}x{prp[3]} D={prp[4]}"""
        people = [(text), (prp[5]), (prp[6])]
        self.tree.insert('', END, values=people)

    def start_tubes(self):
        tubes = Create_Tube()
        tbs = tubes.open()

        text = f"""Столбы"""

    def start_kalitka(self):
        a = Create_kalitka()



if __name__ == "__main__":
    app = App()
    app.mainloop()


# add = Button(root, text='add', command=add)
# add.grid(column=3, row=15)
# s = Label(root, text=f'{PrPsumalls}')
# s.grid(column=0, row=0)

# root.mainloop()
"""btn = Button(tab1, text="Расчет", command=prcount)
btn.grid(column=3, row=5)"""