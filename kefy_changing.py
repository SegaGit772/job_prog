import json
from tkinter import *


def read(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)  # принимает файловый объект и возвращает json объект


def write(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


"""Функция изменения КЭФов"""
def read_write(value_seb, value_sale, link, key, key1, key2):
    with open("kalitka_kefyy.json", "r") as file:
        data = json.load(file)
    data[f"{link}"][f"{key}"][f"{key1}"] = value_seb
    data[f"{link}"][f"{key}"][f"{key2}"] = value_sale
    with open("kalitka_kefyy.json", 'w') as file:
        json.dump(data, file, indent=4)


"""Функция изменения цен"""
def read_write_prices(value, link, key):
    with open("kalitka_kefyy.json", "r") as file:
        data = json.load(file)
    data[f"{link}"][f"{key}"] = value
    with open("kalitka_kefyy.json", "w") as file:
        json.dump(data, file, indent=4)


class Kef_changing(Toplevel):
    file_name = 'kalitka_kefyy.json'  # название json файла

    def __init__(self):
        super().__init__()
        """Шапка"""
        self.name = Label(self, text="Название").grid(column=0, row=2)
        self.seb = Label(self, text="К.себес").grid(column=1, row=2)
        self.sale = Label(self, text="К.продаж").grid(column=2, row=2)

        """КЭФ себестоимость калитки row=5"""
        self.kalitka_labl = Label(self, text="Калитка").grid(column=0, row=5)
        self.kalitka_kef_seb_get = read(Kef_changing.file_name)["kefy"]["kalitka"]["seb"]
        self.kalitka_kef_seb_input = DoubleVar()
        self.kalitka_kef_seb_input.set(self.kalitka_kef_seb_get)
        self.kalitka_seb = Spinbox(self, from_=0.00, to=111.00, width=7, increment=0.01, textvariable=self.kalitka_kef_seb_input)
        self.kalitka_seb.grid(column=1, row=5)
        """КЭФ продажи калитки"""
        self.kalitka_kef_sale_get = read('kalitka_kefy.json')["kalitka"]["sale"]
        self.kalitka_kef_sale_input = DoubleVar()
        self.kalitka_kef_sale_input.set(self.kalitka_kef_sale_get)
        self.kalitka_sale = Spinbox(self, from_=0, to=111, width=7, increment=0.01, textvariable=self.kalitka_kef_sale_input)
        self.kalitka_sale.grid(column=2, row=5)

        """КЭФ себестоимость ВР row=6"""
        self.vr_labl = Label(self, text="ВР").grid(column=0, row=6)
        self.vr_kef_seb_get = read(Kef_changing.file_name)["kefy"]["VR"]["seb"]
        self.vr_kef_seb_input = DoubleVar()
        self.vr_kef_seb_input.set(self.vr_kef_seb_get)
        self.vr_seb = Spinbox(self, from_=0.00, to=111.00, width=7, increment=0.01, textvariable=self.vr_kef_seb_input)
        self.vr_seb.grid(column=1, row=6)
        """КЭФ продажи ВР"""
        self.vr_kef_sale_get = read(Kef_changing.file_name)["kefy"]["VR"]["sale"]
        self.vr_kef_sale_input = DoubleVar()
        self.vr_kef_sale_input.set(self.vr_kef_sale_get)
        self.vr_sale = Spinbox(self, from_=0, to=111, width=7, increment=0.01, textvariable=self.vr_kef_sale_input)
        self.vr_sale.grid(column=2, row=6)

        """КЭФ себестоимость ВО row=7"""
        self.vo_labl = Label(self, text="ВО").grid(column=0, row=7)
        self.vo_kef_seb_get = read(Kef_changing.file_name)["kefy"]["VO"]["seb"]
        self.vo_kef_seb_input = DoubleVar()
        self.vo_kef_seb_input.set(self.vo_kef_seb_get)
        self.vo_seb = Spinbox(self, from_=0.0, to=111.0, width=7, increment=0.01, textvariable=self.vo_kef_seb_input)
        self.vo_seb.grid(column=1, row=7)
        """КЭФ продажи ВО"""
        self.vo_kef_sale_get = read(Kef_changing.file_name)["kefy"]["VO"]["sale"]
        self.vo_kef_sale_input = DoubleVar()
        self.vo_kef_sale_input.set(self.vo_kef_sale_get)
        self.vo_sale = Spinbox(self, from_=0, to=111, width=7, increment=0.01, textvariable=self.vo_kef_sale_input)
        self.vo_sale.grid(column=2, row=7)

        """КЭФ себестоимость Кр (кронштейн) row=8"""
        self.kr_labl = Label(self, text="Кр").grid(column=0, row=8)
        self.kr_kef_seb_get = read(Kef_changing.file_name)["kefy"]["KR"]["seb"]
        self.kr_kef_seb_input = DoubleVar()
        self.kr_kef_seb_input.set(self.kr_kef_seb_get)
        self.kr_seb = Spinbox(self, from_=0.0, to=111.0, width=7, increment=0.01, textvariable=self.kr_kef_seb_input)
        self.kr_seb.grid(column=1, row=8)
        """КЭФ продажи Кр"""
        self.kr_kef_sale_get = read(Kef_changing.file_name)["kefy"]["KR"]["sale"]
        self.kr_kef_sale_input = DoubleVar()
        self.kr_kef_sale_input.set(self.kr_kef_sale_get)
        self.kr_sale = Spinbox(self, from_=0, to=111, width=7, increment=0.01, textvariable=self.kr_kef_sale_input)
        self.kr_sale.grid(column=2, row=8)

        """КЭФы на столбы, фланцы, противоподкоп и косынки есть в json файле, добавлять не стал"""

        """Стоимость косынки"""
        self.kosynka_labl = Label(self, text="Косынка").grid(column=0, row=15)
        self.kosynka_price_get = read('kalitka_kefy.json')["kalitka"]["kosynka"]
        self.kosynka_price_input = IntVar()
        self.kosynka_price_input.set(self.kosynka_price_get)
        self.kosynka_price = Spinbox(self, from_=0, to=10000, width=7, textvariable=self.kosynka_price_input)
        self.kosynka_price.grid(column=1, row=15)

        """Стоимость шарнира"""
        self.sharnir_labl = Label(self, text="Шарнир").grid(column=0, row=14)
        self.sharnir_price_get = read(Kef_changing.file_name)["price"]["sharnir"]
        self.sharnir_price_input = IntVar()
        self.sharnir_price_input.set(self.sharnir_price_get)
        self.sharnir_price = Spinbox(self, from_=0, to=11111, width=7, textvariable=self.sharnir_price_input)
        self.sharnir_price.grid(column=1, row=14)

        """Стоимость краски"""
        self.ral_labl = Label(self, text="RAL").grid(column=0, row=13)
        self.ral_price_get = read(Kef_changing.file_name)["price"]["ral"]
        self.ral_price_input = IntVar()
        self.ral_price_input.set(self.ral_price_get)
        self.ral_price = Spinbox(self, width=7, from_=0, to=111111, textvariable=self.ral_price_input)
        self.ral_price.grid(column=1, row=13)

        """Кнопки"""
        """Кнопка КЭФ себес/продажи калитки"""
        self.s_kal_but = Button(self, text="сохр",
                            command=lambda: read_write(self.kalitka_seb.get(),
                                                       self.kalitka_sale.get(), "kefy", "kalitka", "seb", "sale"))
        self.s_kal_but.grid(column=3, row=5)

        """Кнопка КЭФ себес/продаж ВР"""
        self.s_vr_but = Button(self, text="сохр",
                               command=lambda: read_write(self.vr_seb.get(),
                                                          self.vr_sale.get(), "kefy", "VR", "seb", "sale"))
        self.s_vr_but.grid(column=3, row=6)

        """Кнопка КЭФ себес/продаж ВО"""
        self.s_vo_but = Button(self, text="сохр",
                               command=lambda: read_write(self.vo_seb.get(),
                                                          self.vo_sale.get(), "kefy", "VO", "seb", "sale"))
        self.s_vo_but.grid(column=3, row=7)

        """Кнопка КЭФ себес/продаж Кр"""
        self.s_kr_but = Button(self, text="сохр",
                               command=lambda: read_write(self.kr_seb.get(),
                                                          self.kr_sale.get(), "kefy", "KR", "seb", "sale"))
        self.s_kr_but.grid(column=3, row=8)


        """Кнопка КЭФ продажи калитки"""
        #self.s_kal = Button(self, text="сохр", command=lambda: read_write(self.kalitka_sale.get(), "kalitka", "sale"))
        #self.s_kal.grid(column=3, row=5)

        """Кнопка цены краски"""
        self.s_ral = Button(self, text="сохр", command=lambda: read_write_prices(self.ral_price.get(), "price", "ral"))
        self.s_ral.grid(column=3, row=13)

        """Кнопка цены шарнира"""
        self.s_sharnir = Button(self, text="сохр",
                                command=lambda: read_write_prices(self.sharnir_price.get(), "price", "sharnir"))
        self.s_sharnir.grid(column=3, row=14)

        """Кнопка цены косынки"""
        self.s_kosynka = Button(self, text="сохр",
                                command=lambda: read_write_prices(self.kosynka_price.get(), "price", "kosynka"))
        self.s_kosynka.grid(column=3, row=15)

    def open(self):
        self.grab_set()
        self.wait_window()


if __name__ == "__main__":
    chng = Kef_changing()
    chng.mainloop()
    read()
    write()


"""Добавить КЭФы столбов труб Прп фланцев косынок"""
