from tkinter import *
from math import *
from tkinter import ttk


def multi2(foo, bar):
    return foo * bar


def divide2(foo, bar):
    return foo / bar


def prcount():
    res = round(multi2(int(fenceh.get()), int(fencel.get())) * 0.2 / 1_000_000, 2)
    dyekg.configure(text=f'Расход краски {res}кг')

    foo = multi2((floor(divide2(int(fenceh.get()), int(gridh.get()))) + 1), int(fencel.get()))
    bar = int(fenceh.get()) * (ceil(int(fencel.get()) / int(gridl.get())) + 1)
    baz = round((foo+bar)/1000 * 1.03, 1)   #hlm
    armamkg.configure(text=f'Расход арм {baz}, м')    # расход арматуры в м
    armamm.configure(text=f'Расход арм {round(baz * den * 1000, 1)}, кг')  # расход арматуры в кг

    sumsc = round(baz * int(metprice.get()) * den + res * int(dyeprice.get()) * 0.2, 2)
    fencecost.configure(text=f"Цена секции {sumsc}")
    sumpm = round(sumsc / (int(fencel.get()) / 1000), 1)
    fencecostpm.configure(text=f'Цена пог*м {sumpm}')
    sumall = sumsc * int(amsect.get())
    costnsec.configure(text=f"Цена n секций {sumall}")
    sumallk = round(sumall * float(prkpr.get()))
    sumalls = round(sumall * float(prks.get()))
    fencecostprva.configure(text=f'Цена с К. пр-ва {sumallk}')
    fencecostsale.configure(text=f'Р цена продажи {sumalls}')


def dens(event):
    global den
    den = float(lst[comboExample.current()])   # .current выдаст индекс
    print(den)

window = Tk()
window.title("Расчет всего")
window.geometry('540x420+150+200')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Противоподкоп')
tab_control.add(tab2, text='Столбы')
tab_control.add(tab3, text='Калитки')
tab_control.add(tab4, text='ВР')
tab_control.add(tab5, text='ВО')
tab_control.pack(expand=1, fill='both')

gridd = Label(tab1, text='Высота и длина ячейки')\
    .grid(column=0, row=0)
gridh = Spinbox(tab1, from_=100, to=10000, width=6)
gridh.grid(column=0, row=1)
gridl = Spinbox(tab1, from_=100, to=10000, width=6)
gridl.grid(column=1, row=1)

section = Label(tab1, text='Высота и длина секции')\
    .grid(column=2, row=0)
fencevar = IntVar()
fencevar.set(500)
fenceh = Spinbox(tab1, from_=0, to=10000, width=6, textvariable=fencevar)
fenceh.grid(column=2, row=1)
fencelvar = IntVar()
fencelvar.set(3000)
fencel = Spinbox(tab1, from_=0, to=10000, width=6, textvariable=fencelvar)
fencel.grid(column=3, row=1)

dyelabl = Label(tab1, text='цена краски, руб')\
    .grid(column=0, row=2)
var = IntVar()
var.set(50)
dyeprice = Spinbox(tab1, from_=0, to=600, width=6, textvariable=var)
dyeprice.grid(column=0, row=3)

metdenslabl = Label(tab1, text='Толщина арм')
metdenslabl.grid(column=3, row=2)
metpricelabl = Label(tab1, text='Цена')
metpricelabl.grid(column=1, row=2)
metpricelabl = Label(tab2, text='Цена')
metpricelabl.grid(column=4, row=0)
metprice = Spinbox(tab1, from_=40000, to=500000, width=9)
metprice.grid(column=1, row=3)
amsectlabl = Label(tab1, text="Кол-во секций")
amsectlabl.grid(column=2, row=2)
amsect = Spinbox(tab1, from_=1, to=10000, width=6)
amsect.grid(column=2, row=3)

comboExample = ttk.Combobox(tab1, width=6, values=[
                                                    "6",
                                                    "8",
                                                    "10",
                                                    "12",
                                                    "14",
                                                    "16"])
lst = [0.00022, 0.00040, 0.00062, 0.00089, 0.00121, 0.00158]
comboExample.bind("<<ComboboxSelected>>", dens)
comboExample.grid(column=3, row=3)

prkprlabl = Label(tab1, text='коэф. пр-ва')
prkprlabl.grid(column=1, row=4)
varprkpr = DoubleVar()
varprkpr.set(1.25)
prkpr = Spinbox(tab1, from_=1.00, to=5.00, increment=0.01, width=8, textvariable=varprkpr)
prkpr.grid(column=1, row=5)

prkslabl = Label(tab1, text='коэф. пр-жи')
prkslabl.grid(column=2, row=4)
varprks = DoubleVar()
varprks.set(1.90)
prks = Spinbox(tab1, from_=1.00, to=5.00, increment=0.01, width=8, textvariable=varprks)
prks.grid(column=2, row=5)

btn = Button(tab1, text="Расчет", command=prcount)
btn.grid(column=3, row=5)

dyekg = Label(tab1, width=16, text='Расход краски,   кг')
dyekg.grid(column=0, row=4)

armamkg = Label(tab1, text='Расход арм, м')
armamkg.grid(column=0, row=5)
armamm = Label(tab1, text='Расход арм, кг')
armamm.grid(column=0, row=6)

fencecost = Label(tab1, text="Цена секции")
fencecost.grid(column=0, row=7)
fencecostprva = Label(tab1, text="Цена с К. пр-ва")
fencecostprva.grid(column=1, row=7)
fencecostsale = Label(tab1, text="Р цена продажи")
fencecostsale.grid(column=1, row=8)

fencecostpm = Label(tab1, text="Цена м.пог")
fencecostpm.grid(column=0, row=8)

costnsec = Label(tab1, text=f'Цена n секций')
costnsec.grid(column=0, row=9)

print(__name__)

if __name__ == '__main__':
    window.mainloop()