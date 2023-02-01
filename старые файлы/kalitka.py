from tkinter import *
import sqlite3
import webbrowser
import json

class Kalitka(Toplevel):

    def __init__(self):
        super().__init__()
        self.dict = {1: 680, 2: 60}
        self.zer, w, u = 0, 0, 0
        self.list2, self.list1 = [], []
        self.z = 0
        self.n_data = self.read('datahinge.json')  # потом удалить
        self.nu_data = self.read('dataushki.json')
        self.nk_data = self.read('koefy.json')
        self.bao = self.n_data['hinge'][0]
        self.fao = self.nu_data['ushki'][0]
        self.kkseb = self.nk_data['seb/sale'][0]
        self.kksale = self.nk_data['seb/sale'][1]
        self.ralpr = self.nk_data['seb/sale'][2]

        self.vargt = IntVar()
        self.vargt.set(2000)
        self.var1gt = IntVar()
        self.var1gt.set(1000)
        self.var2gt = IntVar()
        self.var2gt.set(2)
        self.var3gt = IntVar()
        self.var3gt.set(1)

        self.sizeh = Spinbox(self, from_=500, to=5000, increment=50, width=6, textvariable=vargt)
        self.sizew = Spinbox(self, from_=500, to=5000, increment=50, width=6, textvariable=var1gt)
        self.sizeh.grid(column=4, row=0)
        self.sizew.grid(column=5, row=0)

        self.tttubelabl = Label(self, text='0')
        self.ffframelabl = Label(self, text='0')
        self.tttubelabl.grid(column=9, row=2)
        self.ffframelabl.grid(column=9, row=3)

        self.gtwidth1 = Spinbox(self, from_=15, to=400, width=6)
        self.gtwidth2 = Spinbox(self, from_=15, to=400, width=6)
        self.gtwidth3 = Spinbox(self, from_=1.0, to=10.0, width=6)
        self.gtlength1 = Spinbox(self, from_=1.00, to=10.00, width=8, increment=0.01)
        self.gttubeprice = Spinbox(self, from_=40000, to=200000, width=6)
        self.gtamounttube = Spinbox(self, from_=1, to=5, width=4, textvariable=var2gt)
        self.gtamounttube.grid(column=6, row=2)
        self.gtwidth1.grid(column=1, row=2)
        self.gtwidth2.grid(column=2, row=2)
        self.gtwidth3.grid(column=3, row=2)
        self.gtlength1.grid(column=4, row=2)
        self.gttubeprice.grid(column=5, row=2)

        self.gtwidth11 = Spinbox(self, from_=15, to=400, width=6)
        self.gtwidth22 = Spinbox(self, from_=15, to=400, width=6)
        self.gtwidth33 = Spinbox(self, from_=1.0, to=10.0, width=6)
        self.gtlength11 = Spinbox(self, from_=1.00, to=10.00, width=8, increment=0.01)
        self.gtpriceframe = Spinbox(self, from_=40000, to=200000, width=6)
        self.gtamountframe = Spinbox(self, from_=1, to=5, width=4, textvariable=var3gt)
        self.gtamountframe.grid(column=6, row=3)
        self.gtwidth11.grid(column=1, row=3)
        self.gtwidth22.grid(column=2, row=3)
        self.gtwidth33.grid(column=3, row=3)
        self.gtlength11.grid(column=4, row=3)
        self.gtpriceframe.grid(column=5, row=3)
        self.gtwidth1labl = Label(self, text='Большая').grid(column=1, row=1)
        self.gtwidth2labl = Label(self, text='Меньшая').grid(column=2, row=1)
        self.gtwidth3labl = Label(self, text='Толщина').grid(column=3, row=1)
        self.gtlength1labl = Label(self, text='Длина, м').grid(column=4, row=1)
        self.gttubepricelabl = Label(self, text='Цена/т').grid(column=5, row=1)
        self.text = Label(self, text="Введи В/Ш:").grid(column=3, row=0)
        self.gtamounttubelabl = Label(self, text="Кол-во").grid(column=6, row=1)
        self.gtwidthlabl = Label(self, text="Опора").grid(column=0, row=2)
        self.gtwidthlabl1 = Label(self, text="Рама").grid(column=0, row=3)
        self.gttubemquant = Label(self, text="0", width=15)
        self.gttubemquant.grid(column=7, row=0, columnspan=4)
        self.gtframemquant = Label(self, text="0", width=15)
        self.gtframemquant.grid(column=7, row=1, columnspan=4)
        self.buttonaddtube = Button(self, text="Add", command=self.addtube)
        self.buttoncleantube = Button(self, text="C", command=self.cleantube)
        self.buttonframe = Button(self, text="Add", command=self.addframe)
        self.buttoncleanframe = Button(self, text="C", command=self.cleanframe)
        self.buttonaddtube.grid(column=7, row=2)
        self.buttoncleantube.grid(column=8, row=2)
        self.buttonframe.grid(column=7, row=3)
        self.buttoncleanframe.grid(column=8, row=3)

        self.size = Label(self, text='Размер:').grid(column=1, row=4, columnspan=2)
        self.sumlabl = Label(self, width=8, text='Цена').grid(column=3, row=4)
        self.quantity = Label(self, text='Кол-во:').grid(column=4, row=4)

        self.gtzaglprice = Entry(self, width=8)
        self.gtzaglprice.grid(column=3, row=5)

        self.gtzagl = Label(self, text='Заглуш:').grid(column=0, row=5)
        self.phlaneclabl = Label(self, text='Фланец').grid(column=0, row=6)
        self.phlanecsize = Entry(self, width=10).grid(column=1, row=6, columnspan=2)
        self.phlanecprice = Spinbox(self, from_=0, to=10000, width=6)
        self.phlaneamount = Spinbox(self, from_=0, to=10000, width=6)

        self.kosynkilabl = Label(self, text='Косынки').grid(column=0, row=7)
        self.kosynkisize = Entry(self, width=10).grid(column=1, row=7, columnspan=2)
        self.kosynkiprice = Spinbox(self, from_=0, to=10000, width=6)
        self.kosynkiamount = Spinbox(self, from_=0, to=10000, width=6)

        self.ralabl = Label(self, text="РАЛ").grid(column=0, row=8)
        self.vargt = IntVar()
        self.vargt.set(ralpr)
        self.ralprice = Spinbox(self, from_=0, to=1000, textvariable=self.vargt, width=6)
        self.ralprice.grid(column=3, row=8)

        self.panellabl = Label(self, text='Панель').grid(column=0, row=9)
        self.panelsize = Entry(self, width=14).grid(column=1, row=9, columnspan=2)
        self.panelprice = Spinbox(self, from_=0, to=10000, width=6)
        self.panelamount = Spinbox(self, from_=0, to=5, width=6)

        self.panellabl1 = Label(self, text='Панель').grid(column=0, row=10)
        self.panelsize1 = Entry(self, width=14).grid(column=1, row=10, columnspan=2)
        self.panelprice1 = Spinbox(self, from_=0, to=10000, width=6)
        self.panelamount1 = Spinbox(self, from_=0, to=5, width=6)

        self.hingelabl = Label(self, text="Шарнир").grid(column=0, row=11)
        self.hingesize = Entry(self, width=10).grid(column=1, row=11, columnspan=2)
        self.var3gt = IntVar()
        self.var3gt.set(bao)
        self.hingeprice = Spinbox(self, from_=0, to=10000, textvariable=self.var3gt, width=6)
        self.hingevargt = IntVar()
        self.hingevargt.set(2)
        self.hinge = Spinbox(self, from_=0, to=1000, width=6, textvariable=self.hingevargt)

        self.ushkilabl = Label(self, text='Ушки').grid(column=0, row=12)
        self.var4gt = IntVar()
        self.var4gt.set(fao)
        self.ushkiprice = Spinbox(self, from_=0, to=10000, textvariable=self.var4gt, width=6)
        self.ushkiamount = Spinbox(self, from_=0, to=1000, textvariable=self.var2gt, width=6)

        self.ugoloklabl = Label(self, text='Уголок') \
            .grid(column=0, row=13)
        self.sumvargt = IntVar()
        self.sumvargt.set(0)
        self.ugolokprice = Spinbox(self, from_=0, to=10000, width=6, textvariable=self.sumvargt)
        self.ugolokamount = Spinbox(self, from_=0, to=1000, width=6, textvariable=self.sumvargt)
        self.ugoloksize = Entry(self, width=14).grid(column=1, row=13, columnspan=2)

        self.sum = Entry(self, width=6, font="Arial 10")
        self.price = Label(self, text='Материал:')
        self.ksalecost = Label(self, text='0', font="Arial 10")
        self.kprvacost = Label(self, text='0', font="Arial 10")
        self.vargtkpr = DoubleVar()
        self.vargtkpr.set(kkseb)
        self.kprva = Spinbox(self, from_=0, to=10, width=6, increment=0.01, textvariable=self.vargtkpr)
        self.vargtks = DoubleVar()
        self.vargtks.set(kksale)
        self.ksale = Spinbox(self, from_=0, to=10, width=6, increment=0.01, textvariable=self.vargtks)
        self.kprvalabl = Label(self, text='Себест').grid(column=4, row=14)
        self.ksalelabl = Label(self, text='Стоимость').grid(column=5, row=14)

        self.panelamount.grid(column=4, row=9)
        self.panelprice.grid(column=3, row=9)
        self.panelamount1.grid(column=4, row=10)
        self.panelprice1.grid(column=3, row=10)
        self.phlaneamount.grid(column=4, row=6)
        self.phlanecprice.grid(column=3, row=6)
        self.kosynkiamount.grid(column=4, row=7)
        self.kosynkiprice.grid(column=3, row=7)
        self.hingeprice.grid(column=3, row=11)
        self.ushkiprice.grid(column=3, row=12)
        self.ushkiamount.grid(column=4, row=12)
        self.ksalecost.grid(column=5, row=16)
        self.kprvacost.grid(column=4, row=16)
        self.sum.grid(column=3, row=16)
        self.hinge.grid(column=4, row=11)
        self.price.grid(column=3, row=14)
        self.kprva.grid(column=4, row=15)
        self.ksale.grid(column=5, row=15)
        self.ugolokprice.grid(column=3, row=13)
        self.ugolokamount.grid(column=4, row=13)
        self.buttonstart = Button(self, text='Расчет', command=self.gatecount)
        self.buttonushkiS = Button(self, text='S', command=self.ushkiS, wraplength=1)
        self.buttonhingeS = Button(self, text='S', command=self.hingeS, wraplength=1)
        self.buttonkefyS = Button(self, text='S', command=self.kefy, wraplength=1)
        self.buttonstart.grid(column=6, row=13)
        self.buttonhingeS.grid(column=5, row=11)
        self.buttonushkiS.grid(column=5, row=12)
        self.buttonkefyS.grid(column=6, row=15)

    def open(self):
        self.grab_set()
        self.wait_window()

    def gatecount(self):
        a = b = c = 0
        try:
            w1 = int(self.gtwidth1.get())
            w2 = int(self.gtwidth2.get())
            w3 = float(self.chgtocomas(self.gtwidth3.get()))
            w11 = int(self.gtwidth11.get())
            w22 = int(self.gtwidth22.get())
            w33 = float(self.chgtocomas(self.gtwidth33.get()))
            con = sqlite3.connect("denstest6rows.db")
            cursor = con.cursor()
            query = f"""select Density, zaglushka from test where Width={w1} and Length={w2} and Thickness={w3}"""
            query1 = f"""select Density from test where Width={w11} and length={w22} and Thickness={w33}"""
            cursor.execute(query)
            records = cursor.fetchall()
            for elem in records:
                a = elem[0]
                b = elem[1]
            cursor.execute(query1)
            records1 = cursor.fetchall()
            for elem in records1:
                c = elem[0]

            self.gtzaglprice.delete(0, END)
            self.gtzaglprice.insert(0, f'{b}')
            self.tttubelabl.configure(text=f'{self.multi3(a, int(self.gttubeprice.get()), z)}')
            self.ffframelabl.configure(text=f'{self.multi3(a, int(self.gtpriceframe.get()), zer)}')
            self.sum.delete(0, 'end')  # multi(плотн * цена *
            print(z)
            self.sum.insert(0, f'''{
            (int(self.multi3(a, float(self.gttubeprice.get()), z)) +
            self.multi3(c, float(self.gtpriceframe.get()), zer) +
            self.multi2(int(self.self.phlanecprice.get()), int(self.phlaneamount.get())) +
            self.multi2(int(self.kosynkiprice.get()), int(self.kosynkiamount.get())) +
            self.multi2(int(self.hingeprice.get()), int(self.hinge.get())) +
            self.multi2(int(self.panelprice.get()), float(self.panelamount.get())) +
            self.multi2(int(self.panelprice1.get()), float(self.panelamount1.get())) +
            self.multi2(int(self.ushkiprice.get()), int(self.ushkiamount.get())) +
            self.multi2(int(self.ugolokprice.get()), int(self.ugolokamount.get())) +
            self.multi2(b, float(self.gtamounttube.get())) +
            (self.multi3(int(self.sizeh.get()), int(self.sizew.get()), int(self.ralprice.get())) / 1_000_000 * 0.2))
            }''')

            self.kprvacost.configure(text=f'{round((float(self.sum.get())) * float(self.kprva.get()))}')
            self.ksalecost.configure(text=f'{round((float(self.sum.get())) * float(self.ksale.get()))}')
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if con:
                con.close()
                print("Соединение с SQLite закрыто")

    def multi2(self, foo, bar):
        return foo * bar

    def multi2div1(self, foo, bar, baz):
        return foo * bar / baz

    def divide2(self, foo, bar):
        return foo / bar

    def multi3(self, foo, bar, baz):
        return foo * bar * baz

    def chgtocomas(self, foobar):
        return foobar.replace(',', '.')

    def addtube(self):
        self.gttubemquant.configure(text=f'{self.multiply(float(self.chgtocomas(self.gtlength1.get())), int(self.gtamounttube.get()))}')

    def cleantube(self):
        self.gttubemquant.configure(text='0')
        global z, list1
        list1.clear()
        z = 0

    def addframe(self):
        self.gtframemquant.configure(text=f'{self.multiplier(float(self.chgtocomas(self.gtlength11.get())), int(self.gtamountframe.get()))}')

    def cleanframe(self):
        self.gtframemquant.configure(text='0')
        global zer, list2
        list2.clear()
        zer = 0

    def hingeS(self):
        n_data = {'hinge': [self.hingeprice.get()]}
        self.write(n_data, 'datahinge.json')

    def ushkiS(self):
        nu_data = {'ushki': [self.ushkiprice.get()]}
        self.write(nu_data, 'dataushki.json')

    def kefy(self):
        nk_data = {"seb/sale": [self.kprva.get(), self.ksale.get(), sef.ralprice.get()]}
        self.write(nk_data, 'koefy.json')

    def multiply(self, x, y):
        global z, list1
        z += x * y
        list1.append(x * y)
        return z, list1

    def multiplier(self, x, y):
        global zer, list2
        zer += x * y
        list2.append(x * y)
        return zer, list2

