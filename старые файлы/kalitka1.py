from tkinter import *
import sqlite3


class Kalitka(Toplevel):

    @staticmethod
    def __init__(self):
        super().__init__()
        """Шапка расчета"""
        self.text = Label(self, text="Введи В/Ш:").grid(column=2, row=0)
        self.width1_labl = Label(self, text='Большая').grid(column=1, row=1)
        self.width2_labl = Label(self, text='Меньшая').grid(column=2, row=1)
        self.width3_labl = Label(self, text='Толщина').grid(column=3, row=1)
        self.length1_labl = Label(self, text='Длина, м').grid(column=4, row=1)
        self.pricelabl = Label(self, text='Цена/т').grid(column=5, row=1)
        self.amounttubelabl = Label(self, text="Кол-во").grid(column=6, row=1)
        """Ввод высоты и ширины"""
        self.height_kalitki = Entry(self, width=10)
        self.height_kalitki.grid(column=3, row=0)
        self.width_kalitki = Entry(self, width=10)
        self.width_kalitki.grid(column=4, row=0)
        """Столбы и рама"""
        self.tube_labl = label(self, text='Столбы').grid(column=0, row=2)
        self.




if __name__=="__main__":
    kalitka = Kalitka()
    kalitka.mainloop()