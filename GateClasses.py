from tkinter import *
import sqlite3
import json
from kefy_changing import Kef_changing
import webbrowser
from math import ceil



class Details(Toplevel):
    def __init__(self, parent, vars):
        super().__init__(parent)
        self.vars = vars
        self.geometry("150x300")
        """Раскрываем словарь, раскидываем значения по переменным"""
        self.width_1 = int(vars["Столб 1"])
        self.width_2 = int(vars["Столб 2"])
        self.rama_1 = int(vars["Рама 1"])
        self.rama_2 = int(vars["Рама 2"])
        self.flanec = int(Create_gate.null_check(vars["Фланец"]))
        self.kosynka = int(Create_gate.null_check(vars["Косынка"]))
        self.sharnir = int(Create_gate.null_check(vars["Шарнир"]))
        self.zagl = int(Create_gate.null_check(vars["Заглушка"]))
        self.panel1 = int(Create_gate.null_check(vars["Панель 1"]))
        self.panel2 = int(Create_gate.null_check(vars["Панель 2"]))
        self.ugolok = int(Create_gate.null_check(vars["Уголок"]))
        self.anyth = int(Create_gate.null_check(vars["Чтонть"]))
        self.ral = int(Create_gate.null_check(vars["РАЛ"]))

        """Присваиваем Label`ам эти значения и выводим на экран"""
        self.width_1_1_labl = Label(self, text="Столб №1").grid(column=0, row=0)
        self.width_1_1 = Label(self, text=f"{self.width_1}")
        self.width_1_1.grid(column=1, row=0)
        self.width_1_2_labl = Label(self, text="Столб №2").grid(column=0, row=1)
        self.width_1_2 = Label(self, text=f"{self.width_2}")
        self.width_1_2.grid(column=1, row=1)

        self.rama_1_labl = Label(self, text="Рама №1").grid(column=0, row=2)
        self.rama_1 = Label(self, text=f"{self.rama_1}")
        self.rama_1.grid(column=1, row=2)
        self.rama_2_labl = Label(self, text="Рама №2").grid(column=0, row=3)
        self.rama_2 = Label(self, text=f"{self.rama_2}")
        self.rama_2.grid(column=1, row=3)
        self.flanec_labl = Label(self, text="Фланец").grid(column=0, row=4)
        self.flanec_pr = Label(self, text=f"{self.flanec}")
        self.flanec_pr.grid(column=1, row=4)
        self.kosynka_labl = Label(self, text="Косынка").grid(column=0, row=5)
        self.kosynka_pr = Label(self, text=f"{self.kosynka}")
        self.kosynka_pr.grid(column=1, row=5)

        self.sharnir_labl = Label(self, text="Шарнир").grid(column=0, row=6)
        self.sharnir_pr = Label(self, text=f"{self.sharnir}")
        self.sharnir_pr.grid(column=1, row=6)

        self.zagl_labl = Label(self, text="Заглушка").grid(column=0, row=7)
        self.zagl_pr = Label(self, text=f"{self.zagl}")
        self.zagl_pr.grid(column=1, row=7)

        self.panel_1_labl = Label(self, text="Панель 1").grid(column=0, row=8)
        self.panel_1_pr = Label(self, text=f"{self.panel1}")
        self.panel_1_pr.grid(column=1, row=8)

        self.panel_2_labl = Label(self, text="Панель 2").grid(column=0, row=9)
        self.panel_2_pr = Label(self, text=f"{self.panel2}")
        self.panel_2_pr.grid(column=1, row=9)

        self.ugolok_labl = Label(self, text="Уголок").grid(column=0, row=10)
        self.ugolok_pr = Label(self, text=f"{self.ugolok}")
        self.ugolok_pr.grid(column=1, row=10)

        self.anyth_labl = Label(self, text="Чтонть 1").grid(column=0, row=11)
        self.anyth_pr = Label(self, text=f"{self.anyth}")
        self.anyth_pr.grid(column=1, row=11)

        self.ral_labl = Label(self, text="РАЛ").grid(column=0, row=12)
        self.ral_pr = Label(self, text=f"{self.ral}")
        self.ral_pr.grid(column=1, row=12)

    def chg_labl(self):
        self.grab_set()
        self.wait_window()


class Create_gate(Tk):
    def __init__(self):
        super().__init__()
        # self.geometry("500x500")
        self.title("Ворота")
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

        """Ввод высоты и ширины"""
        self.text = Label(self, text="Введи В/Ш, мм:", width=15, anchor=E)
        self.text.grid(column=0, row=0, columnspan=2)
        self.height_gate = Entry(self, width=8)
        self.height_gate.grid(column=2, row=0)
        self.width_gate = Entry(self, width=8)
        self.width_gate.grid(column=3, row=0)
        self.fill_gen = Button(self, text="Заполнить", command=self.to_fill)
        self.fill_gen.grid(column=4, row=0)

        """Первый столб"""
        self.tube_labl = Label(self, text='Столбы', cursor="hand2", foreground="#1b12c4")
        self.tube_labl.grid(column=0, row=2)

        self.width1_1 = Entry(self, width=8)  # Большая сторона профиля
        self.width1_1.insert(0, '80')
        self.width1_1.grid(column=1, row=2)
        self.width1_2 = Entry(self, width=8)  # Меньшая сторона профиля
        self.width1_2.insert(0, "80")
        self.width1_2.grid(column=2, row=2)
        self.tube_labl.bind("<Button-1>", lambda w0, w1=str(self.width1_1.get()),
                                                 w2=str(self.width1_2.get()): self.open_site_tube(w0, w1, w2))
        self.thick1 = Entry(self, width=8)  # толщина профиля
        self.thick1.insert(0, "2.0")
        self.thick1.grid(column=3, row=2)
        self.length1 = Entry(self, width=8)
        self.length1.grid(column=4, row=2)
        self.amount1 = Entry(self, width=8)
        self.amount1.insert(0, '2')
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

        """Первая рама (Два row оставлены про запас"""
        self.rama_labl = Label(self, text='Рама', cursor="hand2", foreground="#1b12c4")
        self.rama_labl.grid(column=0, row=6)

        self.shirina_ramy1_1 = Entry(self, width=8)
        self.shirina_ramy1_1.insert(0, '60')
        self.shirina_ramy1_1.grid(column=1, row=6)
        self.shirina_ramy1_2 = Entry(self, width=8)
        self.shirina_ramy1_2.insert(0, "40")
        self.shirina_ramy1_2.grid(column=2, row=6)
        self.rama_labl.bind("<Button-1>",
                            lambda w0, w1=str(self.shirina_ramy1_1.get()),
                                   w2=str(self.shirina_ramy1_2.get()): self.open_site_tube(w0, w1, w2))
        self.tolshina_ramy_1 = Entry(self, width=8)
        self.tolshina_ramy_1.insert(0, "1.5")
        self.tolshina_ramy_1.grid(column=3, row=6)
        self.dlina_ramy_1 = Entry(self, width=8)
        self.dlina_ramy_1.grid(column=4, row=6)
        self.amount_ramy_1 = Entry(self, width=8)
        self.amount_ramy_1.insert(0, "1")
        self.amount_ramy_1.grid(column=5, row=6)
        self.price_ramy_1 = Entry(self, width=8)
        self.price_ramy_1.insert(0, "90000")
        self.price_ramy_1.grid(column=6, row=6, pady=5)

        """Вторая рама"""
        self.shirina_ramy2_1 = Entry(self, width=8)
        self.shirina_ramy2_1.grid(column=1, row=7)
        self.shirina_ramy2_2 = Entry(self, width=8)
        self.shirina_ramy2_2.grid(column=2, row=7)
        self.tolshina_ramy_2 = Entry(self, width=8)
        self.tolshina_ramy_2.insert(0, "")
        self.tolshina_ramy_2.grid(column=3, row=7)
        self.dlina_ramy_2 = Entry(self, width=8)
        self.dlina_ramy_2.grid(column=4, row=7)
        self.amount_ramy_2 = Entry(self, width=8)
        self.amount_ramy_2.insert(0, "")
        self.amount_ramy_2.grid(column=5, row=7)
        self.price_ramy_2 = Entry(self, width=8)
        self.price_ramy_2.insert(0, "90000")
        self.price_ramy_2.grid(column=6, row=7, pady=5)

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
        self.kosynka_size.insert(0, "45x55x5")
        self.kosynka_amount = Entry(self, width=8)
        self.kosynka_amount.grid(column=5, row=11)
        self.kosynka_price = Entry(self, width=8)
        self.kosynka_price.grid(column=6, row=11)

        "Шарниры"
        self.sharnir_labl = Label(self, width=9, text="Шарнир", anchor=W).grid(column=0, row=12)
        self.sharnir_size = Entry(self, width=11)
        self.sharnir_size.grid(column=3, row=12, columnspan=2, sticky=E, padx=6)
        self.sharnir_amount = Entry(self, width=8)
        self.sharnir_amount.grid(column=5, row=12)
        self.sharnir_amount.insert(0, "4")
        self.sharnir_price = Entry(self, width=8)
        self.sharnir_price.grid(column=6, row=12)

        "Заглушки"
        self.zagl_labl = Label(self, width=9, text="Заглушка", anchor=W).grid(column=0, row=13)
        self.zagl_size = Entry(self, width=11)
        self.zagl_size.grid(column=3, row=13, columnspan=2, padx=6, sticky=E)
        self.zagl_amount = Entry(self, width=8)
        self.zagl_amount.grid(column=5, row=13)
        self.zagl_amount.insert(0, "2")
        self.zagl_price = Entry(self, width=8)
        self.zagl_price.grid(column=6, row=13)

        """Панели"""
        self.panel_labl = Label(self, width=9, text="Панель", anchor=W).grid(column=0, row=14)
        self.panel_size = Entry(self, width=11)
        self.panel_size.grid(column=3, row=14, columnspan=2, sticky=E, padx=6)
        self.panel_amount = Entry(self, width=8)
        self.panel_amount.grid(column=5, row=14)
        self.panel_price = Entry(self, width=8)
        self.panel_price.grid(column=6, row=14)

        """Панели"""
        self.panel_labl2 = Label(self, width=9, text="Панель доб.", anchor=W).grid(column=0, row=15)
        self.panel_size2 = Entry(self, width=11)
        self.panel_size2.grid(column=3, row=15, columnspan=2, sticky=E, padx=6)
        self.panel_amount2 = Entry(self, width=8)
        self.panel_amount2.grid(column=5, row=15)
        self.panel_price2 = Entry(self, width=8)
        self.panel_price2.grid(column=6, row=15)

        """Уголок"""
        self.ug_labl = Label(self, width=9, text="Уголок", anchor=W).grid(column=0, row=16)
        self.ug_size = Entry(self, width=11)
        self.ug_size.grid(column=3, row=16, columnspan=2, sticky=E, padx=6)
        self.ug_amount = Entry(self, width=8)
        self.ug_amount.grid(column=5, row=16)
        self.ug_price = Entry(self, width=8)
        self.ug_price.grid(column=6, row=16)

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
        self.ral_price = Entry(self, width=8)
        self.ral_price.grid(column=6, row=18)

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
        self.count_det_but.grid(column=2, columnspan=2, row=22)
        self.change_kefy = Button(self, width=13, text="Изменить КЭФы", command=self.kefy)
        self.change_kefy.grid(column=2, columnspan=2, row=23)

    def open_site_tube(self, event, w1, w2):
        foo = "https://www.spk.ru/catalog/metalloprokat/trubniy-prokat/truba-profilnaya/?rt02[]="
        bar = "&rt03[]="
        baz = foo + w1 + bar + w2
        webbrowser.open(baz)

    def details(self):
        window = Details(self, vars)
        window.chg_labl()

    """Ф изменения коэффициентов"""
    def kefy(self):
        window = Kef_changing()
        a = window.open()

    """Ф заменяет точки на запятую у толщин металлов, только у них. 
    В остальных случаях значение после запятой отбрасывается"""

    @staticmethod
    def chgtocomas(foo):
        return foo.replace(",", ".")

    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    """Извлекаем данные из БД"""
    def database(self, width1, width2, thick):
        try:
            sqlite_connection = sqlite3.connect('dens_db.db')
            cursor = sqlite_connection.cursor()
            sqlite_select_query = (f"""
                                        SELECT Density from test where Width={width1} 
                                        and Length={width2} and Thickness={thick}
                                    """)
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            for elem in records:
                density = elem[0]
            return density

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite___", error, "вернул 0")
            """Если передаются пустые ячейки (как например во втором столбе или второй раме), то вернет 0. ОКей"""
            return 0

        except UnboundLocalError:
            return float(self.read("new_dens.json")["new_dens"])

        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    """Обработчик событий если поступает '' значение"""
    @staticmethod
    def null_check(foo):
        try:
            return float(foo)
        except:
            return 0

    def count(self):
        """Расчет стоимости столбов. Try обрабатывает событие если поступает '' пустой значение"""
        global vars

        cena_tube_1 = (int(
            (self.database(str(self.width1_1.get()), str(self.width1_2.get()), self.chgtocomas(str(self.thick1.get()))))
            * int(self.length1.get()) / 1000 * float(self.amount1.get()) * float(self.price_tube1.get())))
        try:
            cena_tube_2 = (int(
            float(self.database(str(self.width2_1.get()), str(self.width2_2.get()),
            self.chgtocomas(str(self.thick2.get())))) * int(self.length2.get()) / 1000 *
            float(self.amount2.get()) * float(self.price_tube2.get())
            ))
        except:
            cena_tube_2 = 0

        cena_ramy_1 = (int(
            float(self.database(str(self.shirina_ramy1_1.get()), str(self.shirina_ramy1_2.get()),
            self.chgtocomas(str(self.tolshina_ramy_1.get()))))
            * int(self.dlina_ramy_1.get()) / 1000 * float(self.amount_ramy_1.get()) * float(self.price_ramy_1.get())
            ))

        try:
            cena_ramy_2 = (int(
            float(self.database(str(self.shirina_ramy2_1.get()), str(self.shirina_ramy2_2.get()),
            self.chgtocomas(str(self.tolshina_ramy_2.get())))) * int(self.dlina_ramy_2.get()) / 1000 * float(
            self.amount_ramy_2.get()) * float(self.price_ramy_2.get())
            ))
        except:
            cena_ramy_2 = 0

        flanec = int(self.null_check(self.flanec_price.get()) * self.null_check(self.flanec_amount.get()))
        print(flanec)
        kosynka = int(self.null_check(self.kosynka_price.get()) * self.null_check(self.kosynka_amount.get()))
        sharnir = int(self.null_check(self.sharnir_price.get()) * self.null_check(self.sharnir_amount.get()))
        zagl = int(self.null_check(self.zagl_price.get()) * self.null_check(self.zagl_amount.get()))
        panel_1 = int(self.null_check(self.panel_price.get()) * self.null_check(self.panel_amount.get()))
        panel_2 = int(self.null_check(self.panel_price2.get()) * self.null_check(self.panel_amount2.get()))
        ugolok = int(self.null_check(self.ug_price.get()) * self.null_check(self.ug_amount.get()))
        anyth = int(self.null_check(self.any_price.get()) * self.null_check(self.any_amount.get()))
        ral = int((
                int(self.ral_price.get()) * int(self.height_gate.get()) * int(self.width_gate.get()) / 1000000 * 0.2
                   ))

        """Создаем переменную vars для передачи словаря в окно Детали расчета"""
        vars = {"Столб 1": cena_tube_1, "Столб 2": cena_tube_2, "Рама 1": cena_ramy_1, "Рама 2": cena_ramy_2,
                "Фланец": flanec, "Косынка": kosynka, "Шарнир": sharnir,
                "Заглушка": zagl, "Панель 1": panel_1, "Панель 2": panel_2,
                "Уголок": ugolok, "Чтонть": anyth, "РАЛ": ral}

        """Расчет стоимости остального"""
        cena_stuff = (flanec + kosynka + sharnir + zagl + panel_1 + panel_2 + ugolok + anyth + ral)

        """расчет итоговых значений"""
        summa = cena_stuff + cena_ramy_2 + cena_ramy_1 + cena_tube_2 + cena_tube_1
        k_seb = self.read("kalitka_kefyy.json")["kefy"]["VR"]["seb"]
        k_sale = self.read("kalitka_kefyy.json")["kefy"]["VR"]["sale"]
        summa_k_seb = int(summa * float(k_seb))
        summa_k_sale = int(summa * float(k_sale))
        self.summa_seb_text.config(text=f"{summa_k_seb}")
        self.summa_sale_text.config(text=f"{summa_k_sale}")
        self.summa_text.config(text=f"{summa}")

    """Начальное заполнение окон по нажатию кнопки. Если одна из сторон больше 2,4м то толщина столба 3"""
    def to_fill(self):
        height = int(self.height_gate.get())
        height1000 = height + 1000
        width = int(self.width_gate.get())
        width_stvorki = width / 2
        ukosina = 0

        if height > 2399 or width > 4798:
            """1. Удалить старое значение. Ввести новое"""
            self.thick1.delete(0, last=END)
            self.thick1.insert(0, "3.0")
            """укосина - делим на 100, возводим в сил и умножаем на 100, чтоб округлить 3230 до 3300"""
            ukosina = ceil(((height ** 2 + width_stvorki ** 2) ** 0.5) / 100) * 100
            rama_amount = height * 4 + width * 2 + ukosina * 2
            self.dlina_ramy_1.delete(0, last=END)
            self.dlina_ramy_1.insert(0, f"{rama_amount}")
        else:
            rama_amount = height * 4 + width * 2
            self.dlina_ramy_1.delete(0, last=END)
            self.dlina_ramy_1.insert(0, f"{rama_amount}")
            self.length1.delete(0, last=END)
            self.length1.insert(0, f"{height1000 * 2}")

        self.length1.delete(0, last=END)
        self.length1.insert(0, f"{height1000 * 2}")

        w1_1 = int(self.width1_1.get())
        w1_2 = int(self.width1_2.get())
        if w1_1 == 60 and w1_2 == 60:
            self.flanec_size.delete(0, last=END)
            self.flanec_size.insert(0, "150x150x5")
        elif w1_1 in [60, 80] and w1_2 in [60, 80]:
            self.flanec_size.delete(0, last=END)
            self.flanec_size.insert(0, "200x200x5")
        else:
            None
        height__30 = (height-70)    # height__30 - высота панели
        self.panel_size.delete(0, last=END)
        self.panel_size.insert(0, "{}х".format(height__30))  # разобраться с автозаполнением панелей

        """Заполнение строки Заглушка. Если такой заглушки в БД нет, удалит существующие записи в строке"""
        try:
            zaglushka = self.read("kalitka_kefyy.json")["zaglushki"][f"{str(self.width1_1.get())}x{str(self.width1_2.get())}"]
            self.zagl_price.delete(0, last=END)
            self.zagl_price.insert(0, f"{zaglushka}")
            self.zagl_size.delete(0, last=END)
            self.zagl_size.insert(0, f"{w1_1}x{w1_2}")
        except KeyError:
            self.zagl_price.delete(0, last=END)
            self.zagl_size.delete(0, last=END)
            self.zagl_amount.delete(0, last=END)

        """Устанавливаем цену краски"""
        ral = self.read("kalitka_kefyy.json")["price"]["ral"]
        self.ral_price.delete(0, last=END)
        self.ral_price.insert(0, f"{ral}")

        """Загружаем с json цену косынки"""
        cena = self.read("kalitka_kefyy.json")["price"]["kosynka"]
        self.kosynka_price.delete(0, last=END)
        self.kosynka_price.insert(0, f"{cena}")

        """Загружаем с json цену шарнира"""
        cena = self.read("kalitka_kefyy.json")["price"]["sharnir"]
        self.sharnir_price.delete(0, last=END)
        self.sharnir_price.insert(0, f"{cena}")


if __name__ == "__main__":
    a = Create_gate()
    a.mainloop()


"""1. Упоры в землю 
2. ушки
3. Не считает металлы
"""