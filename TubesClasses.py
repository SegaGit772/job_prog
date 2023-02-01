from tkinter import *
import sqlite3
import json
import webbrowser
from Kclasses import Density_set_class
# уголок и круглые столбы швеллера

class Tubes(Toplevel):
    def __init__(self):
        super().__init__()
        self.width1 = Spinbox(self, from_=15, to=400, width=6)
        self.width1.grid(column=0, row=1)
        self.width1labl = Label(self, text='Большая')
        self.width1labl.grid(column=0, row=0)
        self.width2 = Spinbox(self, from_=15, to=400, width=6)
        self.width2.grid(column=1, row=1)
        self.width2labl = Label(self, text='Меньшая')
        self.width2labl.grid(column=1, row=0)
        self.thickness = Spinbox(self, from_=1.0, to=10.0, width=6)
        self.thickness.grid(column=2, row=1)
        self.thicknesslabl = Label(self, text='Толщина')
        self.thicknesslabl.grid(column=2, row=0)
        self.length1 = Spinbox(self, from_=0.1, to=100.0, width=8)
        self.length1.grid(column=3, row=1)
        self.length1labl = Label(self, text='Длина, м').grid(column=3, row=0)
        self.tubeprice = Spinbox(self, from_=40000, to=200000, width=8)
        self.tubeprice.grid(column=4, row=1)
        self.tubepricelabl = Label(self, text='Цена/т', cursor='hand2', foreground='#1b12c4')
        self.tubepricelabl.grid(column=4, row=0)
        self.tubepricelabl.bind('<Button-1>', self.callback)
        self.tubestart = Button(self, text='Расчет', command=self.tubecount, width=7)
        self.tubestart.grid(column=2, row=7)
        self.roundtube = Button(self, text='кр.труба', command=self.chngtoround)
        self.roundtube.grid(column=6, row=2)
        self.tubecostlabl = Label(self, text='Стоимость').grid(column=7, row=0)
        self.tubecostlabll = Label(self, text='')
        self.tubecostlabll.grid(column=7, row=1)

        """Строка Заглушка"""
        self.asdd = StringVar()
        self.asdd.set('Заглушка')
        self.zaglushka = Entry(self, textvariable=self.asdd, width=10)
        self.zaglushka.grid(column=1, row=2)
        self.zaglushkaprice = Label(self, text='')
        self.zaglushkaprice.grid(column=7, row=2)
        self.zaglushkalabl = Label(self, text="Заглушка")
        self.zaglushkalabl.grid(column=0, row=2)

        """Строка РАЛ"""
        self.var = IntVar()
        self.var.set(370)
        self.dyepricetube = Spinbox(self, from_=0, to=1000, textvariable=self.var, width=6)
        self.dyepricetube.grid(column=4, row=3)
        self.dyeamount = Spinbox(self, from_=1, to=10, width=4)
        self.dyeamount.grid(column=3, row=3)
        self.dyepricetubelabl = Label(self, text='')
        self.dyepricetubelabl.grid(column=7, row=3)
        self.dyelabl = Label(self, text="РАЛ")
        self.dyelabl.grid(column=0, row=3)

        """Строка Фланец"""
        self.phlanec = Entry(self, width=10)
        self.phlanec.grid(column=1, row=4)
        self.phlanecprice = Spinbox(self, from_=0, to=100000, width=6)   # цена фланца
        self.phlanecprice.grid(column=4, row=4)
        self.phlaneclabl = Label(self, text="Фланец", width=7, anchor=W)
        self.phlaneclabl.grid(column=0, row=4)
        self.phlaneccost = Label(self, text="0")       # Стоимость фланца
        self.phlaneccost.grid(column=7, row=4)

        """Строка Косынка"""
        self.kosynkilabl = Label(self, text="Косынки")
        self.kosynkilabl.grid(column=0, row=5)
        self.kosynki = Entry(self, width=10)       # размер косынок
        self.kosynki.grid(column=1, row=5)
        self.kosynkiam = Spinbox(self, width=4, from_=0, to=10000)      # кол-во косынок
        self.kosynkiam.grid(column=3, row=5)
        self.kosynkiprice = Spinbox(self, width=6, from_=1, to=10000)    # Цена косынки
        self.kosynkiprice.grid(column=4, row=5)
        self.kosynkicost = Label(self, width=6, text="0")   # стоимость косынок
        self.kosynkicost.grid(column=7, row=5)

        """Строка Разное"""
        self.another_labl = Label(self, text="Разное", width=7, anchor=W).grid(column=0, row=6)
        self.another = Entry(self, width=10)
        self.another.grid(column=1, row=6)
        self.anotheramount = Spinbox(self, from_=1, to=10, width=4)
        self.anotheramount.grid(column=3, row=6)
        self.anotherprice = Spinbox(self, from_=0, to=10000, width=6)
        self.anotherprice.grid(column=4, row=6)

        self.ksaletubeprvalabl = Label(self, text="коэф.пр-ва").grid(column=3, row=8)
        self.sebes = Label(self, text='материалы').grid(column=3, row=7)

        self.br = self.read('tubes_kefy_seb_sale.json')
        self.br = self.br["seb"]
        self.var = DoubleVar()
        self.var.set(self.br)
        self.kprvasaletube = Spinbox(self, from_=1.00, to=10.00, increment=0.01, width=8, textvariable=self.var)
        self.kprvasaletube.grid(column=4, row=8)
        self.ksaletubesalelabl = Label(self, text="коэф.пр-жи")
        self.ksaletubesalelabl.grid(column=3, row=9)

        self.pr = self.read('tubes_kefy_seb_sale.json')
        self.pr = self.pr["sale"]
        self.var1 = DoubleVar()
        self.var1.set(self.pr)
        self.ksaletubesale = Spinbox(self, from_=1.00, to=10.00, increment=0.01, width=8, textvariable=self.var1)
        self.ksaletubesale.grid(column=4, row=9)

        """Лейблы вывода результата"""
        self.tubesummlabl = Label(self, text='0')
        self.tubesummlabl.grid(column=7, row=7)
        self.tubecostprva = Label(self, text='0')
        self.tubecostprva.grid(column=7, row=8)
        self.tubecostsale = Label(self, text="0")
        self.tubecostsale.grid(column=7, row=9)

        """Кнопка сохранения КЭФа в json-файл"""
        self.buttonkprs = Button(self, text='S', command=self.kprs, width=2, state="disabled")
        self.buttonkprs.grid(column=6, row=8)

        """Ставим спинкбокс КЭФа фланца и лейбл"""
        """Было сделано единственное правильное решение чтоб каждый сам выставлял себе коэффициенты без отдельного
        окна для фланца и косынки. Тогда и кнопка сохранения не нужна, у нас просто по умолчанию будет 1,15 и 1,85"""
        """        self.flanec_kef_labl = Label(self, text="фланец").grid(column=1, row=8)
        self.flanec_kef_get = self.read("kalitka_kefyy.json")["kefy"]["flanec"]
        self.flanec_kef_var = DoubleVar()
        self.flanec_kef_var.set(self.flanec_kef_get)
        self.flanec_kef_but = Spinbox(self, from_=0, to=11, increment=0.01, width=8, textvariable=self.flanec_kef_var)
        self.flanec_kef_but.grid(column=2, row=8)

        self.kosynka_kef_get = self.read("kalitka_kefyy.json")["kefy"]["kosynka"]
        self.kosynka_kef_var = DoubleVar()
        self.kosynka_kef_var.set(self.kosynka_kef_get)
        self.kosynka_kef_but = Spinbox(self, from_=0.00, to=11, increment=0.01, width=8, textvariable=self.kosynka_kef_var)
        self.kosynka_kef_but.grid(column=2, row=9)"""
# наверх до "ставим спинбокс КЭФа..." пока не работает надо разобраться где хранить кэфы фланца и косынки
# решил работает-не трогай

    def read(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self, data, filename):
        data = json.dumps(data)  # сериализует obj питон в строку str json
        data = json.loads(str(data))  # сериализует строку формата json в строку формата питон
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def kprs(self):
        kpv_data = {'seb': self.kprvasaletube.get()}  # создание переменной, где хранится словарь из нового значения
        ksl_data = {'sale': self.ksaletubesale.get()}
        self.write(kpv_data, 'tubes_kefy_seb_sale.json')  # Ф write с этим словарем и документ куда сохраним
        self.write(ksl_data, 'tubes_kefy_seb_sale.json')

    def chngtoround(self):    # дописать sql и расчет круглых труб и прочего
        self.width1.destroy()
        self.width2.destroy()
        self.width1labl.destroy()
        self.width2labl.destroy()
        self.widthlabl = Label(self, text='Диаметр трубы,мм', anchor='center', width=15).grid(column=0, columnspan=2, row=0)
        self.width = Spinbox(self, from_=0, to=500, width=14)
        self.width.grid(column=0, row=1, columnspan=2)

    def tubecount(self):
        a = b = 0
        try:
            sqlite_connection = sqlite3.connect('denstest6rows.db')
            cursor = sqlite_connection.cursor()
            width1 = str(self.width1.get())
            width2 = str(self.width2.get())
            thickness = str(self.chgtocomas(self.thickness.get()))
            sqlite_select_query = (f"""
                                    SELECT Density, zaglushka from test where Width={width1} 
                                    and Length={width2} and Thickness={thickness}""")
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            for elem in records:
                a = elem[0]
                b = elem[1]
            if b == 0:
                self.zagl_price_set()
            cursor.close()
            tube_price = round(int(self.tubeprice.get()) * float(a) * float(self.chgtocomas(self.length1.get())), 1)
            self.tubecostlabll.configure(text=f'{tube_price}')
            self.zaglushka.delete(0, END)
            self.zaglushka.insert(0, f"{width1}x{width2}")
            self.zaglushkaprice.configure(text=f'{b}')
            ral_price = round(
                int(self.dyepricetube.get()) * ((int(width1) * 2 + int(width2) * 2) / 1000 *
                float(self.chgtocomas(self.length1.get()))) * 0.2 * int(self.dyeamount.get()), 1)
            self.dyepricetubelabl.configure(text=f'{ral_price}')
            self.phlaneccost.configure(text=f"{str(self.phlanecprice.get())}")
            e = int(self.kosynkiam.get()) * int(self.kosynkiprice.get())
            self.kosynkicost.configure(text=f"{e}")  # kosynkiam  price

            f = round(tube_price + b + ral_price + int(self.phlanecprice.get()) + e, 1)
            self.tubesummlabl.configure(text=f'{f}')
            self.tubecostprva.configure(text=f'{round(f * float(self.kprvasaletube.get()), 1)}')
            self.tubecostsale.configure(text=f'{round(f * float(self.ksaletubesale.get()), 1)}')
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    def chgtocomas(self, foobar):
        return foobar.replace(',', '.')

    def zagl_price_set(self):
        zagl = Zaglushka(self)
        zaglprice = zagl.open_price()
        print(zaglprice)

    def open(self):
        self.grab_set()
        self.wait_window()


    """Метод открывает сайт спк с нужными размерами трубы"""
    def callback(self, event):
        foo = "https://www.spk.ru/catalog/metalloprokat/trubniy-prokat/truba-profilnaya/?rt02[]="
        bar = "&rt03[]="
        baz = foo + self.width1.get() + bar + self.width2.get()
        webbrowser.open(baz)



"""Если не находит заглушку в БД, то откроет это окно с просьбой ввести ее цену"""
class Zaglushka(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.zaglprice = IntVar()
        self.label = Label(self, text='Укажите цену заглушки')
        self.label.pack()
        self.entry_price = Entry(self, textvariable=self.zaglprice)
        self.entry_price.pack()
        self.button = Button(self, text='Ok', command=self.destroy)
        self.button.pack()

    def open_price(self):
        self.grab_set()
        self.wait_window()
        zaglprice = self.zaglprice.get()
        return zaglprice

if __name__ == "__main__":
    tubes = Tubes()
    tubes.mainloop()

"""
1. КЭФы фланца и косынки и как их добавлять к расчету столба    ----- решение - пусть рукой вводят в те два окна
2. Прекол в том что у нас цена заглушки которую я ввожу не переносится в расчет программы
"""