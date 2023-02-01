from tkinter import *
# from tkinter import ttk
from PrPclasses import PrP
from PrPclasses import PrPsumalls


root = Tk()
root.title('Расчет себестоимости')
root.geometry('200x200+150+200')


def startPrP():
    windowPrP = PrP()


def startTubes():
    #WindowTubes = Tubes()
    pass


def add():
    ...



def open_window():
    ...


addPrP = Button(root, text='ПрП', command=startPrP)
addPrP.grid(column=1, row=15)

addTubes = Button(root, text='Трубы', command=startTubes)
addTubes.grid(column=2, row=15)

add = Button(root, text='add', command=add)
add.grid(column=3, row=15)
s = Label(root, text=f'{PrPsumalls}')
s.grid(column=0, row=0)

root.mainloop()
"""btn = Button(tab1, text="Расчет", command=prcount)
btn.grid(column=3, row=5)"""