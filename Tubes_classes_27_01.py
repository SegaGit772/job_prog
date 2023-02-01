from tkinter import *
from tkinter import ttk
import sqlite3
import json
import webbrowser
from Kclasses import Density_set_class


class Details(Toplevel):
    def __init__(self, parent, vars):
        super().__init__(parent)
        self.vars = vars
        self.geometry("200x300")

        """Раскрываем словарь, раскидываем значения по переменным"""
        self.width_1 = int(vars["Столб 1"])
        self.width_2 = int(vars["Столб 2"])
        self.flanec = int(vars["Фланец"])
        self.kosynka = int(vars["Косынка"])
        self.zagl = int(vars["Заглушка"])
        self.anyth = int(vars["Чтонть"])
        self.ral = int(vars["РАЛ"])

        """Присваиваем Label`ам эти значения и выводим на экран"""
        self.width_1_1_labl = Label(self, text="Столб №1").grid(column=0, row=0)
        self.width_1_1 = Label(self, text=f"{self.width_1}")
        self.width_1_1.grid(column=1, row=0)

        self.width_1_2_labl = Label(self, text="Столб №2").grid(column=0, row=1)
        self.width_1_2 = Label(self, text=f"{self.width_2}")
        self.width_1_2.grid(column=1, row=1)

        self.flanec_labl = Label(self, text="Фланец").grid(column=0, row=4)
        self.flanec_pr = Label(self, text=f"{ self.flanec}")
        self.flanec_pr.grid(column=1, row=4)

        self.kosynka_labl = Label(self, text="Косынка").grid(column=0, row=5)
        self.kosynka_pr = Label(self, text=f"{self.kosynka}")
        self.kosynka_pr.grid(column=1, row=5)

        self.anyth_labl = Label(self, text="Чтонть 1").grid(column=0, row=11)
        self.anyth_pr = Label(self, text=f"{self.anyth}")
        self.anyth_pr.grid(column=1, row=11)

        self.ral_labl = Label(self, text="РАЛ").grid(column=0, row=12)
        self.ral_pr = Label(self, text=f"{self.ral}")
        self.ral_pr.grid(column=1, row=12)


        self.zagl_labl = Label(self, text="Заглушка").grid(column=0, row=14)
        self.zagl_pr = Label(self, text=f"{self.zagl}")
        self.zagl_pr.grid(column=1, row=14)

    def chg_labl(self):
        self.grab_set()
        self.wait_window()


class Create_Tube(Tk):
    def __init__(self):
        types = ["Прямоуг", "Уголки", "Круглые"]
        super().__init__()
        self.title("Опоры")
        # если например в text не указать self то этот объект создастся в окне main2

        """Шапка"""
        self.width1_labl = Label(self, text='Большая').grid(column=1, row=1)
        self.width2_labl = Label(self, text='Меньшая').grid(column=2, row=1)
        self.width3_labl = Label(self, text='Толщина').grid(column=3, row=1)
        self.length1_labl = Label(self, text='Длина,мм').grid(column=4, row=1)
        self.amounttubelabl = Label(self, text="Кол-во")
        self.amounttubelabl.grid(column=5, row=1, ipadx=5, ipady=0)  # отсутпы наебашить. если ___.grid то объект возвращает нан и ipad не работает
        self.pricelabl = Label(self, text='Цена/т')
        self.pricelabl.grid(column=6, row=1, ipadx=11)

        """Первый столб"""
        self.combo_tube_1 = ttk.Combobox(self, width=7, values=types)
        self.combo_tube_1.grid(column=0, row=2)
        self.combo_tube_1.current(0)
        self.combo_tube_2 = ttk.Combobox(self, width=7, values=types)
        self.combo_tube_2.grid(column=0, row=3)
        self.combo_tube_2.current(0)
        self.tube_labl = Label(self, text='Столбы', cursor="hand2", foreground="#1b12c4")
        self.tube_labl.grid(column=0, row=1)

        self.width1_1 = Entry(self, width=8)  # Большая сторона профиля
        self.width1_1.insert(0, '60')
        self.width1_1.grid(column=1, row=2)
        self.width1_2 = Entry(self, width=8)  # Меньшая сторона профиля
        self.width1_2.insert(0, "60")
        self.width1_2.grid(column=2, row=2)
        self.tube_labl.bind("<Button-1>", lambda w0, w1=str(self.width1_1.get()),
                                                 w2=str(self.width1_2.get()): self.open_site_tube(w0, w1, w2))
        self.thick1 = Entry(self, width=8)  # толщина профиля
        self.thick1.insert(0, "1.5")
        self.thick1.grid(column=3, row=2)
        self.length1 = Entry(self, width=8)
        self.length1.grid(column=4, row=2)
        self.amount1 = Entry(self, width=8)
        self.amount1.insert(0, '1')
        self.amount1.grid(column=5, row=2)
        self.price_tube1 = Entry(self, width=8)
        self.price_tube1.insert(0, "90000")
        self.price_tube1.grid(column=6, row=2)

        """Второй столб"""
        self.width2_1 = Entry(self, width=8)
        self.width2_1.grid(column=1, row=3)
        self.width2_2 = Entry(self, width=8)
        self.width2_2.grid(column=2, row=3)
        self.thick2 = Entry(self, width=8)
        self.thick2.grid(column=3, row=3)
        self.length2 = Entry(self, width=8)
        self.length2.grid(column=4, row=3)
        self.amount2 = Entry(self, width=8)
        self.amount2.grid(column=5, row=3)
        self.price_tube2 = Entry(self, width=8)
        self.price_tube2.insert(0, "90000")
        self.price_tube2.grid(column=6, row=3, pady=5)

        """Фланец"""
        self.flanec_labl = Label(self, width=9, text="Фланец", anchor=W).grid(column=0, row=10)
        self.flanec_size = Entry(self, width=11)
        self.flanec_size.grid(column=3, row=10, columnspan=2, sticky=E, padx=6)
        self.flanec_amount = Entry(self, width=8)
        self.flanec_amount.grid(column=5, row=10)
        self.flanec_price = Entry(self, width=8)
        self.flanec_price.grid(column=6, row=10)

        """Косынки"""
        self.kosynka_labl = Label(self, width=9, text="Косынка", anchor=W).grid(column=0, row=11)
        self.kosynka_size = Entry(self, width=11)
        self.kosynka_size.grid(column=3, row=11, columnspan=2, sticky=E, padx=6)
        self.kosynka_amount = Entry(self, width=8)
        self.kosynka_amount.grid(column=5, row=11)
        self.kosynka_price = Entry(self, width=8)
        self.kosynka_price.grid(column=6, row=11)

        "Заглушки"
        self.zagl_labl = Label(self, width=9, text="Заглушка", anchor=W).grid(column=0, row=13)
        self.zagl_size = Entry(self, width=11)
        self.zagl_size.grid(column=3, row=13, columnspan=2, padx=6, sticky=E)
        self.zagl_amount = Entry(self, width=8)
        self.zagl_amount.grid(column=5, row=13)
        self.zagl_amount.insert(0, "1")
        self.zagl_price = Entry(self, width=8)
        self.zagl_price.grid(column=6, row=13)

        """Что-нибудь"""
        self.any_labl = Label(self, width=9, text="....", anchor=W).grid(column=0, row=17)
        self.any_size = Entry(self, width=11)
        self.any_size.grid(column=3, row=17, columnspan=2, sticky=E, padx=6)
        self.any_amount = Entry(self, width=8)
        self.any_amount.grid(column=5, row=17)
        self.any_price = Entry(self, width=8)
        self.any_price.grid(column=6, row=17)

        """РАЛ"""
        self.ral_labl = Label(self, text="Краска", width=9, anchor=W).grid(column=0, row=18)
        self.ral_user_cost = Entry(self, width=34)
        self.ral_user_cost.grid(column=2, row=18, columnspan=3)
        self.ral_user_cost.insert(0, "Или введи здесь стоимость покраски")
        self.ral_amount = Entry(self, width=8)
        self.ral_amount.grid(column=5, row=18)
        self.ral_amount.insert(0, '1')
        self.ral_price = Entry(self, width=8)
        self.ral_price.grid(column=6, row=18)
        self.ral_price.insert(0, "370")

        """Вывод результата расчета"""
        self.summa_text = Label(self)
        self.summa_text.grid(column=6, row=21)
        self.summa_seb_text = Label(self)
        self.summa_seb_text.grid(column=6, row=22)
        self.summa_sale_text = Label(self)
        self.summa_sale_text.grid(column=6, row=23)

        """Надписи текстовые: Сумма, себестоимость, рекоменд цена"""
        self.summa = Label(self, text="Сумма", anchor=E, width=20)
        self.summa.grid(column=4, row=21, columnspan=2)
        self.summa_seb = Label(self, text='Себест. продукции', anchor=E, width=20)
        self.summa_seb.grid(column=4, row=22, columnspan=2)
        self.summa_sale = Label(self, text='Реком. цена продажи', anchor=E, width=20)
        self.summa_sale.grid(column=4, row=23, columnspan=2)

        """Кнопки Расчет, Детали расчета и Изменить КЭФы"""
        self.count_but = Button(self, text="Рассчитать", width=13, command=self.count)
        self.count_but.grid(column=2, columnspan=2, row=21)
        self.count_det_but = Button(self, width=13, text="Детали расчета",  command=self.details, state="active") # disabled
        self.count_det_but.grid(column=0, columnspan=2, row=21)

        """Лейбл кэфов 1 и 2 для труб и уголков"""
        self.kef1 = Entry(self)
        self.kef1.insert(0, "1")
        self.kef2 = Entry(self)
        self.kef2.insert(0, "1")

        """Спинбоксы КЭФов"""
        self.k_seb = Spinbox(self, from_=1.15, to=22, width=8, increment=0.01)
        self.k_seb.grid(column=2, columnspan=2, row=22)
        self.k_sale = Spinbox(self, from_=1.85, to=22, increment=0.01, width=8)
        self.k_sale.grid(column=2, columnspan=2, row=23)

    def open_site_tube(self, event, w1, w2):
        foo = "https://www.spk.ru/catalog/metalloprokat/trubniy-prokat/truba-profilnaya/?rt02[]="
        bar = "&rt03[]="
        baz = foo + w1 + bar + w2
        webbrowser.open(baz)

    def details(self):
        window = Details(self, vars)
        window.chg_labl()

    """Ф заменяет точки на запятую у толщин металлов, только у них. 
    В остальных случаях значение после запятой отбрасывается"""
    @staticmethod
    def chgtocomas(foo):
        return foo.replace(",", ".")

    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    """Извлекаем данные из БД"""
    def database(self, width1, width2, thickness, kef):
        try:
            sqlite_connection = sqlite3.connect('dens_db.db')
            cursor = sqlite_connection.cursor()
            sqlite_select_query = (f"""
                                        SELECT density from densities where width1={width1} 
                                        and width2={width2} and thickness={thickness} and kef={kef};
                                    """)
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            for elem in records:
                density = elem[0]
            return density

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite___", error, "вернул 0")
            return 0

        except UnboundLocalError:
            print("UnboundLocalError__")
            window = Density_set_class()
            window.density_set()
            return float(self.read("new_dens.json")["new_dens"])

        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    def null_check(self, foo):
        try:
            return float(foo)
        except:
            return 0

    def count(self):
        global vars, results

        # всегда будем просто передавать 0 при вызове database у круглых труб и еще создать labl откуда будет извлекаться
        # кеф 1 и 2 у уголков, этот кеф будет меняться при нажатии кнопки "Уголок"
        """Переменные для передачи в окно mainwindow"""
        combo_w_1 = self.combo_tube_1.get()
        combo_w_2 = self.combo_tube_2.get()


        """Переменные первой опоры"""
        width1_1 = int(self.width1_1.get())
        width1_2 = int(self.width1_2.get())
        thickness1 = float(self.chgtocomas(self.thick1.get()))
        tube_price1 = int(self.price_tube1.get())
        length1 = int(self.length1.get())
        kef1 = int(self.kef1.get())
        amount1 = int(self.amount1.get())

        """Переменные второй опоры"""
        width2_1 = int(self.null_check(self.width2_1.get()))
        width2_2 = int(self.null_check(self.width2_2.get()))
        thickness2 = float(self.null_check(self.chgtocomas(self.thick2.get())))
        tube_price2 = int(self.null_check(self.price_tube2.get()))
        length2 = int(self.null_check(self.length2.get()))
        kef2 = int(self.kef2.get())
        amount2 = int(self.null_check(self.amount2.get()))

        """Остальные переменные"""
        zagl_price = float(self.null_check(self.zagl_price.get()))
        zagl_amount = int(self.null_check(self.zagl_amount.get()))
        zagl_cost = zagl_amount * zagl_price
        flanec_amount = int(self.null_check(self.flanec_amount.get()))
        flanec_price = float(self.null_check(self.flanec_price.get()))
        flanec_cost = int(flanec_amount * flanec_price)
        flanec_name = self.flanec_size.get()
        ral_price = int(self.ral_price.get())
        kosynka_price = float(self.null_check(self.kosynka_price.get()))
        kosynka_amount = int(self.null_check(self.kosynka_amount.get()))
        kosynka_cost = int(kosynka_price * kosynka_amount)
        kosynka_name = self.kosynka_size.get()
        ral_user_price = self.ral_user_cost.get()
        ral_amount = int(self.ral_amount.get())
        any_price = int(self.null_check(self.any_price.get()))
        any_amount = int(self.null_check(self.any_amount.get()))
        any_cost = any_price * any_amount
        ral_user_price2 = 0
        ral_user_price1 = 0

        results = {"combo_w_1": combo_w_1, "width1_1": width1_1, "width1_2": width1_2, "thick1": thickness1,
                   "flanec": flanec_name, "kosynka": kosynka_name,
                   "combo_w_2": combo_w_2, "width2_1": width2_1, "width2_2": width2_2, "thick2": thickness2}

        """Два условия меняю kef1 и kef2 в зависимости от выбранных значених. Это влияет на правильное извлечение
        данных из БД"""
        if self.combo_tube_1.get() in ["Прямоуг", "Круглые"]:
            kef1 = 1
        else:
            kef1 = 2
        if self.combo_tube_2.get() in ["Прямоуг", "Круглые"]:
            kef2 = 1
        else:
            kef2 = 2

        tube_1_dens = self.database(width1=width1_1, width2=width1_2, thickness=thickness1, kef=kef1)

        try:
            tube_2_dens = self.database(width1=width2_1, width2=width2_2, thickness=thickness2, kef=kef2)
        except:
            tube_2_dens = 0

        tube_1_cost = tube_1_dens * tube_price1 * length1 / 1000 * amount1
        tube_2_cost = tube_2_dens * tube_price2 * length2 / 1000 * amount2

        try:
            ral_user_price1 = int(self.ral_user_cost.get())
            # ral_user_price1 = int(ral_user_price) * ral_amount
        except ValueError:
            if width1_2 == 0:
                ral_user_price1 = 2 * 3.14 * width1_1 / 2000 * length1 / 1000 * 0.2 * ral_price
            else:
                ral_user_price1 = int(
                    int(self.width1_1.get()) * 4 / 1000 * length1 / 1000 * ral_amount * ral_price * 0.2)
            if width2_2 == 0:
                ral_user_price2 = 2 * 3.14 * width2_1 / 2000 * length2 / 1000 * 0.2 * ral_price
            else:
                ral_user_price2 = int(width2_1 * 4 / 1000 * ral_amount * length2 / 1000 * ral_price * 0.2)

        ral_user_price = ral_user_price2 + ral_user_price1

        summa = int(tube_1_cost + tube_2_cost + zagl_cost + flanec_cost +
                 kosynka_cost + ral_user_price + any_cost)


        k_prva_summa = int(summa * float(self.k_seb.get()))
        k_sale_summa = int(summa * float(self.k_sale.get()))
        self.summa_text.configure(text=f"{summa}")
        self.summa_seb_text.configure(text=f'{k_prva_summa}')
        self.summa_sale_text.configure(text=f"{k_sale_summa}")

        """Создаем переменную vars для передачи словаря в окно Детали расчета"""
        vars = {"Столб 1": tube_1_cost, "Столб 2": tube_2_cost, "Заглушка": zagl_cost,
                "Фланец": flanec_cost, "Косынка": kosynka_cost, "Чтонть": any_cost,
                 "РАЛ": ral_user_price}



    def open(self):
        self.grab_set()
        self.wait_window()
        """return (combo_w_1, width_count_1_1, width_count_1_2,
                combo_w_2, width_count_2_1, width_count_2_1)"""
        return results

if __name__ == "__main__":
    a = Create_Tube()
    a.mainloop()

"""
1. Добавить расчет стыковки столбов
2. Круглые трубы уголки и швеллера
3. Кароче ебать, в БД есть запись: (0,0,0,0,0) и width2_1, width2_2 изза Ф null_check имеют уже значение 0.
Поэтому sql Запрос вернет мне 0 плотность
4. расчет углов можно оформить по-другому:
присвоить width1_2 значение 1
для кругов значение 0 и искать будет сочно
"""
