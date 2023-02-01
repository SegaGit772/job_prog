from tkinter import *
from tkinter import ttk
from math import floor
from math import ceil


#root = Tk()
#root.title('Расчет себестоимости')
#root.geometry('200x200+150+200')


#def startPrP():
    #windowPrP = PrP()


def startTubes():
    #WindowTubes = Tubes()
    pass


def add():
    ...

class PrP(Toplevel):
    def __init__(self):
        super().__init__()

        self.title('Расчет ПрП')
        self.geometry('540x420+150+200')
        self.gridd = ttk.Label(self, text='Высота и длина ячейки') \
            .grid(column=0, row=0)
        self.gridh = ttk.Spinbox(self, from_=100, to=10000, width=6)  # textvariable=var,
        self.gridh.grid(column=0, row=1)
        self.gridl = ttk.Spinbox(self, from_=100, to=10000, width=6)  # textvariable=var,
        self.gridl.grid(column=1, row=1)
        #self.but = ttk.Button(self, text='Расчет1', command=self.destroy())

        # если self здесь не написать, то на глав
        # экране отображаться кнопка на глав экране сначала не будет а потом появится
        # после метода add
        #self.but.grid(column=4, row=4)
        self.butTrans = ttk.Button(self, text='Перенести', command=self.transfer)
        self.butTrans.grid(column=5, row=4)
        self.section = Label(self, text='Высота и длина секции')\
            .grid(column=2, row=0)
        self.fenceh = Spinbox(self, from_=0, to=10000, width=6)
        self.fenceh.grid(column=2, row=1)
        self.fencel = Spinbox(self, from_=0, to=10000, width=6)
        self.fencel.grid(column=3, row=1)
        self.dyelabl = Label(self, text='цена краски, руб')\
            .grid(column=0, row=2)
        self.dyeprice = Spinbox(self, from_=0, to=600, width=6)
        self.dyeprice.grid(column=0, row=3)
        self.metdenslabl = Label(self, text='Толщина арм')
        self.metdenslabl.grid(column=3, row=2)
        self.metpricelabl = Label(self, text='Цена')
        self.metpricelabl.grid(column=1, row=2)
        self.metprice = Spinbox(self, from_=40000, to=500000, width=9)
        self.metprice.grid(column=1, row=3)
        self.amsectlabl = Label(self, text="Кол-во секций")
        self.amsectlabl.grid(column=2, row=2)
        self.amsect = Spinbox(self, from_=1, to=10000, width=6)
        self.amsect.grid(column=2, row=3)
        self.comboExample = ttk.Combobox(self, width=6, values=[
            "6",
            "8",
            "10",
            "12",
            "14",
            "16"])
        self.lst = [0.00022, 0.00040, 0.00062, 0.00089, 0.00121, 0.00158]
        self.comboExample.bind("<<ComboboxSelected>>", self.dens)
        self.comboExample.grid(column=3, row=3)
        self.prkprlabl = Label(self, text='коэф. пр-ва')
        self.prkprlabl.grid(column=1, row=4)
        self.prkpr = Spinbox(self, from_=1.00, to=5.00, increment=0.01, width=8)
        self.prkpr.grid(column=1, row=5)
        self.prkslabl = Label(self, text='коэф. пр-жи')
        self.prkslabl.grid(column=2, row=4)
        self.prks = Spinbox(self, from_=1.00, to=5.00, increment=0.01, width=8)
        self.prks.grid(column=2, row=5)
        self.btn = Button(self, text="Расчет", command=self.prcount)
        self.btn.grid(column=3, row=5)
        self.dyekg = Label(self, width=16, text='Расход краски,   кг')
        self.dyekg.grid(column=0, row=4)
        self.armamkg = Label(self, text='Расход арм, м')
        self.armamkg.grid(column=0, row=5)
        self.armamm = Label(self, text='Расход арм, кг')
        self.armamm.grid(column=0, row=6)
        self.fencecost = Label(self, text="Цена секции")
        self.fencecost.grid(column=0, row=7)
        self.fencecostprva = Label(self, text="Цена с К. пр-ва")
        self.fencecostprva.grid(column=1, row=7)
        self.fencecostsale = Label(self, text="Р цена продажи")
        self.fencecostsale.grid(column=1, row=8)
        self.fencecostpm = Label(self, text="Цена м.пог")
        self.fencecostpm.grid(column=0, row=8)
        self.costnsec = Label(self, text=f'Цена n секций')
        self.costnsec.grid(column=0, row=9)

    def dens(self, event):
        global den
        den = float(self.lst[self.comboExample.current()])

    def prcount(self):
        global sumalls
        res = round((self.multi2(int(self.fenceh.get()), int(self.fencel.get()))) * 0.2 / 1_000_000, 2)
        self.dyekg.configure(text=f'Расход краски {res}кг')
        foo = self.multi2((floor(self.divide2(int(self.fenceh.get()), int(self.gridh.get()))) + 1), int(self.fencel.get()))
        bar = int(self.fenceh.get()) * (ceil(int(self.fencel.get()) / int(self.gridl.get())) + 1)
        baz = round((foo + bar) / 1000 * 1.03, 1)  # hlm
        self.armamkg.configure(text=f'Расход арм {baz}, м')  # расход арматуры в м
        self.armamm.configure(text=f'Расход арм {round(baz * den * 1000, 1)}, кг')  # расход арматуры в кг
        sumsc = round(baz * int(self.metprice.get()) * den + res * int(self.dyeprice.get()) * 0.2, 2)
        self.fencecost.configure(text=f"Цена секции {sumsc}")
        sumpm = round(sumsc / (int(self.fencel.get()) / 1000), 1)
        self.fencecostpm.configure(text=f'Цена пог*м {sumpm}')
        sumall = sumsc * int(self.amsect.get())
        self.costnsec.configure(text=f"Цена n секций {sumall}")
        sumallk = round(sumall * float(self.prkpr.get()))
        sumalls = round(sumall * float(self.prks.get()))
        self.fencecostprva.configure(text=f'Цена с К. пр-ва {sumallk}')
        self.fencecostsale.configure(text=f'Р цена продажи {sumalls}')
        #self.destroy()


    def open(self):
        self.grab_set()
        self.wait_window()
        a = self.gridl.get()
        return sumalls, a

    def multi2(self, foo, bar):
        return foo * bar

    def divide2(self, foo, bar):
        return foo / bar

    def transfer(self):
        pass

    def summ(self, a):
        print(a)


class App(Tk):
    def __init__(self):
        super().__init__()
        self.addPrP = Button(self, text='ПрП', command=self.open_window)
        self.addPrP.grid(column=1, row=15)
        self.addTubes = Button(self, text='Трубы', command=self.startTubes)
        self.addTubes.grid(column=2, row=15)


    def open_window(self):
        PrPwin = PrP()
        prp = PrPwin.open()
        # print(prp)
        print(type(prp))

    def startTubes(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()


#add = Button(root, text='add', command=add)
#add.grid(column=3, row=15)
#s = Label(root, text=f'{PrPsumalls}')
#s.grid(column=0, row=0)

#root.mainloop()
"""btn = Button(tab1, text="Расчет", command=prcount)
btn.grid(column=3, row=5)"""