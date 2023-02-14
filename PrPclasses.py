from tkinter import *
from tkinter import ttk
from math import floor
from math import ceil
import webbrowser
import json


dict = {'500x2500-150x150': 19.1, '500x3100-150x150': 24.2, '500x3000-150x150': 22.7,
        '300x3100-150x150': 16.1, '300x3000-150x150': 15.5, '300x2500-150x150': 15.5,
        '750x1000-150x150': 10.6, '750x2300-150x150': 24.4}

text = """
Программа считает противоподкопную решетку. \n
1. Коэффициенты пр-ва (производства) и пр-жи(продажи) загружаются\n 
каждый раз из базы данных. Если Кэфы изменятся на постоянной основе,\n
подправьте в приложении и нажмите кнопку "S", так вы перезапишите данные.
"""

class Ref(Tk):
    def __init__(self):
        super().__init__()
        self.title("Справка по ПрП")
        self.geometry("500x200")
        self.labl = Label(self, text=f"{text}", justify=LEFT, width=63)
        self.labl.grid(column=0, row=0)
        self.but = Button(self, text="закрыть", command=self.destroy)
        self.but.grid(column=0, row=1)


class PrP(Toplevel):

    def __init__(self):
        super().__init__()
        self.title('Расчет ПрП')
        self.geometry('430x420+150+200')
        self.gridd = ttk.Label(self, text='Высота и длина ячейки', anchor='center').grid(column=0, row=0, columnspan=2)
        self.gridhvar = IntVar()
        self.gridhvar.set(150)
        self.gridlvar = IntVar()
        self.gridlvar.set(150)
        self.gridh = ttk.Spinbox(self, from_=50, to=1000, width=6, textvariable=self.gridhvar)
        self.gridh.grid(column=0, row=1)
        self.gridl = ttk.Spinbox(self, from_=50, to=1000, width=6, textvariable=self.gridlvar)
        self.gridl.grid(column=1, row=1)
        self.section = Label(self, text='Высота и длина секции', anchor='w').grid(column=2, row=0, columnspan=2)
        self.fenceh = Spinbox(self, from_=0, to=10000, width=6)
        self.fenceh.grid(column=2, row=1)
        self.fencel = Spinbox(self, from_=0, to=10000, width=6)
        self.fencel.grid(column=3, row=1)
        self.dyelabl = Label(self, text='цена краски, руб').grid(column=0, row=2)
        self.dyepricevar = IntVar()
        self.dyepricevar.set(50)
        self.dyeprice = Spinbox(self, from_=0, to=600, width=6, textvariable=self.dyepricevar)
        self.dyeprice.grid(column=0, row=3)
        self.comboExample = ttk.Combobox(self, width=6, values=[
            "6",
            "8",
            "10",
            "12",
            "14",
            "16"])
        self.lst = [0.00022, 0.00040, 0.00062, 0.00089, 0.00121, 0.00158]
        self.comboExample.bind("<<ComboboxSelected>>", self.dens)
        self.comboExample.grid(column=1, row=3)
        self.amsectlabl = Label(self, text="Кол-во секций")
        self.amsectlabl.grid(column=2, row=2)
        self.amsect = Spinbox(self, from_=1, to=10000, width=6)
        self.amsect.grid(column=2, row=3)
        self.metdenslabl = Label(self, text='Толщина арм')
        self.metdenslabl.grid(column=1, row=2)
        self.metpricelabl = Label(self, text='Цена', cursor='hand2', foreground='#1b12c4')
        self.metpricelabl.grid(column=3, row=2)
        self.metpricelabl.bind('<Button-1>', self.callback)
        self.metprice = Spinbox(self, from_=40000, to=500000, width=9)
        self.metprice.grid(column=3, row=3)
        self.prkprlabl = Label(self, text='коэф. пр-ва')
        self.prkprlabl.grid(column=1, row=4)

        self.br = self.read('prp_kefy_seb_sale.json')
        self.br = self.br["seb"]
        self.kpr = DoubleVar()
        self.kpr.set(self.br)
        self.prkpr = Spinbox(self, from_=1.00, to=5.00, increment=0.01, width=8, textvariable=self.kpr)
        self.prkpr.grid(column=1, row=5)
        self.prkslabl = Label(self, text='коэф. пр-жи')
        self.prkslabl.grid(column=2, row=4)

        self.pr = self.read('prp_kefy_seb_sale.json')
        self.pr = self.pr["sale"]
        self.ksl = DoubleVar()
        self.ksl.set(self.pr)
        self.prks = Spinbox(self, from_=1.00, to=5.00, increment=0.01, width=8, textvariable=self.ksl)
        self.prks.grid(column=2, row=5)
        self.btn = Button(self, text="Расчет", command=self.prcount)
        self.btn.grid(column=3, row=5)
        self.dyekg = Label(self, width=16, text='Расход краски,   кг', anchor='w')
        self.dyekg.grid(column=0, row=4)
        self.armamkg = Label(self, text='Расход арм, м', anchor='w', width=16)
        self.armamkg.grid(column=0, row=5)
        self.armamm = Label(self, text='Расход арм, кг', anchor='w', width=16)
        self.armamm.grid(column=0, row=6)
        self.fencecost = Label(self, text="Цена секции", anchor='w', width=16)
        self.fencecost.grid(column=0, row=7)
        self.fencecostprva = Label(self, text="Цена с Коэф. пр-ва")
        self.fencecostprva.grid(column=1, row=7, columnspan=2)
        self.fencecostsale = Label(self, text="Рекоменд цена продажи")
        self.fencecostsale.grid(column=1, row=8, columnspan=2)
        self.fencecostpm = Label(self, text="Цена м.пог", anchor='w', width=16)
        self.fencecostpm.grid(column=0, row=8)
        self.costnsec = Label(self, text=f'Цена n секций', anchor='w', width=17)
        self.costnsec.grid(column=0, row=9)
        self.buttonKprS = Button(self, text='S', command=self.kprS, wraplength=1)
        self.buttonKprS.grid(column=5, row=5)

        """Создаем меню-справки"""
        self.mainmenu = Menu(self)  # создаем экземпляр классе меню и привязываем к виджету, где будет использ.
        self.config(menu=self.mainmenu)  # его опции меню присваивается экземпляр Menu
        self.mainmenu.add_command(label="Справка", command=self.reference)

    def reference(self):
        instance = Ref()


    def read(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self, data, filename):
        data = json.dumps(data)  # сериализует obj питон в строку str json
        data = json.loads(str(data))  # сериализует строку формата json в строку формата питон
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def kprS(self):
        kpv_data = {'seb': self.prkpr.get()}  # создание переменной, где хранится словарь из нового значения
        ksl_data = {'sale': self.prks.get()}
        self.write(kpv_data, 'prp_kefy_seb_sale.json')  # Ф write с этим словарем и документ куда сохраним
        self.write(ksl_data, 'prp_kefy_seb_sale.json')

    def dens(self, event):
        global den
        den = float(self.lst[self.comboExample.current()])

    def prcount(self):
        global sumalls, gridlength, gridheight, amsections, fenceheight, fencelength, thickness
        gridlength = self.gridl.get()
        gridheight = self.gridh.get()
        amsections = self.amsect.get()
        fenceheight = self.fenceh.get()
        fencelength = self.fencel.get()
        thickness = self.comboExample.get()
        ss = f'{self.fenceh.get()}x{self.fencel.get()}-{self.gridh.get()}x{self.gridl.get()}'
        res = round((self.multi2(int(self.fenceh.get()), int(self.fencel.get()))) * 0.2 / 1_000_000, 1)
        self.dyekg.configure(text=f'Расход краски {res}кг')
        if ss in dict:
            rashodarm = dict['500x2500-150x150']
        else:
            foo = self.multi2((floor(self.divide2(int(self.fenceh.get()), int(self.gridh.get()))) + 1), int(self.fencel.get()))
            bar = int(self.fenceh.get()) * (ceil(int(self.fencel.get()) / int(self.gridl.get())) + 1)
            rashodarm = round((foo + bar) / 1000 * 1.03)  # hlm
        self.armamkg.configure(text=f'Расход арм {rashodarm}, м')  # расход арматуры в м
        self.armamm.configure(text=f'Расход арм {round(rashodarm * den * 1000, 0)}, кг')  # расход арматуры в кг
        sumsc = round(rashodarm * int(self.metprice.get()) * den + res * int(self.dyeprice.get()) * 0.2)
        self.fencecost.configure(text=f"Цена секции   {sumsc}")
        sumpm = round(sumsc / (int(self.fencel.get()) / 1000))
        self.fencecostpm.configure(text=f'Цена пог*м     {sumpm}')
        sumall = sumsc * int(self.amsect.get())
        self.costnsec.configure(text=f"Цена n секций {sumall}")
        sumallk = round(sumall * float(self.prkpr.get()))
        sumalls = round(sumall * float(self.prks.get()))
        self.fencecostprva.configure(text=f'Цена с К. пр-ва {sumallk}')
        self.fencecostsale.configure(text=f'Р цена продажи {sumalls}')

    def open(self):
        self.grab_set()
        self.wait_window()
        return fenceheight, fencelength, gridheight, gridlength, thickness, amsections, sumalls

    def callback(self, event):
        site = 'https://www.spk.ru/catalog/metalloprokat/sortovoy-prokat/armatura/?pt01[]=a500c&rt01[]=' + self.comboExample.get()
        webbrowser.open_new(site)

    def multi2(self, foo, bar):
        return foo * bar

    def divide2(self, foo, bar):
        return foo / bar

    def transfer(self):
        pass

    def summ(self, a):
        print(a)


if __name__ == "__main__":
    prp = PrP()
    prp.mainloop()

"""Справка
1. Если вторым окном создать Toplevel, то мы не сможем пользоваться кнопками этого окна, даже закрыть не сможем.
Для этого необходимо перехватить ввод. Сразу после создания класса нового окна ввести
self.grab_set() -   захватываем весь пользовательский ввод
и можно пользоваться окном. Но тогда блокируется основное окно. Значит проще вторым окном создать Tk окно

"""
