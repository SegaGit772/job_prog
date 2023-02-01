from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
people = [('1',2,2222), ('2',4,123123)]
columns = ('name', 'amount', 'cost')
tree = ttk.Treeview(columns=columns, show='headings')
tree.pack(fill=BOTH, expand=1)
tree.heading('name', text='Описание')
tree.heading('amount', text='Кол-во')
tree.heading('cost', text='Стоимость')
for person in people:
    tree.insert('', END, values=person)
root.mainloop()