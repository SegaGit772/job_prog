from tkinter import *
import sqlite3
import json
from kefy_changing import Kef_changing

class Density_set_class(Toplevel):
    def __init__(self):
        super().__init__()
        self.labl = Label(self, text="Введи кг/м металла")
        self.labl.pack()
        self.met_density = Entry(self, width=11)
        self.met_density.pack()
        self.close_but = Button(self, text="OK", command=self.destroy)    #  self.destroy)
        self.close_but.pack()

    def density_set(self):
        self.grab_set()  # чтоб окно получало все события и пользователь не сможет взаимодействовать с осн окном
        self.wait_window()
        print("aaa")  # - этот метод сработал, потом закрывается sql
        met_density1 = self.met_density.get()
        print(met_density1)

        return met_density1


def create_kalitka():

    def details():
        pass

    """Ф изменения коэффициентов"""
    def kefy():
        window = Kef_changing()
        a = window.open()

    """Ф заменяет точки на запятую у толщин металлов, только у них. 
    В остальных случаях значение после запятой отбрасывается"""
    def chgtocomas(foo):
        return foo.replace(",", ".")

    def read(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def database(width1, width2, thick):
        try:
            sqlite_connection = sqlite3.connect('denstest6rows.db')
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

        except (sqlite3.Error) as error:
            print("Ошибка при работе с SQLite___", error, "вернул 0")
            """Если передаются пустые ячейки (как например во втором столбе или второй раме), то вернет 0. ОКей"""
            return 0

        except UnboundLocalError:
            density = Density_set_class()
            density_var = density.density_set()
            #print(density_var)
            return density_var

        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    """Обработчик событий если поступает '' значение"""
    def null_check(foo):
        try:
            return float(foo)
        except:
            return 0

    def count():
        """Расчет стоимости столбов. Try обрабатывает событие если поступает '' пустой значение"""
        cena_tube_1 = (int(
            (database(str(width1_1.get()), str(width1_2.get()), chgtocomas(str(thick1.get()))))
            * int(length1.get()) / 1000 * float(amount1.get()) * float(price_tube1.get())))
        try:
            cena_tube_2 = (int(
            float(database(str(width2_1.get()), str(width2_2.get()), chgtocomas(str(thick2.get()))))
            * int(length2.get()) / 1000 * float(amount2.get()) * float(price_tube2.get())
            ))
        except:
            cena_tube_2 = 0

        cena_ramy_1 = (int(
            float(database(str(shirina_ramy1_1.get()), str(shirina_ramy1_2.get()),
            chgtocomas(str(tolshina_ramy_1.get()))))
            * int(dlina_ramy_1.get()) / 1000 * float(amount_ramy_1.get()) * float(price_ramy_1.get())
            ))

        try:
            cena_ramy_2 = (int(
            float(database(str(shirina_ramy2_1.get()), str(shirina_ramy2_2.get()),
            chgtocomas(str(tolshina_ramy_2.get())))) * int(dlina_ramy_2.get()) / 1000 * float(
            amount_ramy_2.get()) *
            float(price_ramy_2.get())
            ))
        except:
            cena_ramy_2 = 0

        """Расчет стоимости остального"""
        cena_stuff = int((
                      null_check(flanec_price.get()) * null_check(flanec_amount.get()) +
                      null_check(kosynka_price.get()) * null_check(kosynka_amount.get()) +
                      null_check(sharnir_price.get()) * null_check(sharnir_amount.get()) +
                      null_check(zagl_price.get()) * null_check(zagl_amount.get()) +
                      null_check(panel_price.get()) * null_check(panel_amount.get()) +
                      null_check(panel_price2.get()) * null_check(panel_amount2.get()) +
                      null_check(ug_price.get()) * null_check(ug_amount.get()) +
                      null_check(any_price.get()) * null_check(any_amount.get()) +
                      null_check(ral_price.get()) * null_check(height_kalitki.get()) / 1000 *
                      null_check(width_kalitki.get()) / 1000 * 0.2
                      ))
        """расчет итоговых значений"""
        summa = cena_stuff + cena_ramy_2 + cena_ramy_1 + cena_tube_2 + cena_tube_1
        k_seb = read("kalitka_kefy.json")["kalitka"]["seb"]
        k_sale = read("kalitka_kefy.json")["kalitka"]["sale"]
        summa_k_seb = int(summa * float(k_seb))
        summa_k_sale = int(summa * float(k_sale))
        summa_seb_text.config(text=f"{summa_k_seb}")
        summa_sale_text.config(text=f"{summa_k_sale}")
        summa_text.config(text=f"{summa}")

    """Начальное заполнение окон по нажатию кнопки"""
    def to_fill():
        height = int(height_kalitki.get())
        height1000 = height+1000
        if height > 2499:
            """1. Удалить старое значение
            2. Ввести новое"""
            thick1.delete(0, last=END)
            thick1.insert(0, "2")
            length1.delete(0, last=END)
            length1.insert(0, "{}".format(height1000))
        else:
            length1.delete(0, last=END)
            length1.insert(0, "{}".format(height1000))
        width = int(width_kalitki.get()) - 100
        width = width * 2 + height * 2
        dlina_ramy_1.delete(0, last=END)
        dlina_ramy_1.insert(0, "{}".format(width))
        w1_1 = int(width1_1.get())
        w1_2 = int(width1_2.get())
        if w1_1 == 60 and w1_2 == 60:
            flanec_size.delete(0, last=END)
            flanec_size.insert(0, "150x150x5")
        elif w1_1 in [60, 80] and w1_2 in [60, 80]:
            flanec_size.delete(0, last=END)
            flanec_size.insert(0, "200x200x5")
        else:
            None
        height__30 = (height-70)    # height__30 - высота панели
        panel_size.delete(0, last=END)
        panel_size.insert(0, "{}х".format(height__30))  # разобраться с автозаполнением панелей

        """Заполнение строки Заглушка. Если такой заглушки в БД нет, удалит существующие записи в строке"""
        try:
            zaglushka = read("kalitka_kefyy.json")["zaglushki"][f"{str(width1_1.get())}x{str(width1_2.get())}"]
            zagl_price.delete(0, last=END)
            zagl_price.insert(0, f"{zaglushka}")
            zagl_size.delete(0, last=END)
            zagl_size.insert(0, f"{w1_1}x{w1_2}")
        except KeyError:
            zagl_price.delete(0, last=END)
            zagl_size.delete(0, last=END)
            zagl_amount.delete(0, last=END)

        """Устанавливаем цену краски"""
        ral = read("kalitka_kefyy.json")["price"]["ral"]
        ral_price.delete(0, last=END)
        ral_price.insert(0, f"{ral}")

        # сначала заполняю размер калитки и профили столбов, потом жмут заполнить

        """Загружаем с json цену косынки"""
        cena = read("kalitka_kefyy.json")["price"]["kosynka"]
        kosynka_price.delete(0, last=END)
        kosynka_price.insert(0, f"{cena}")

        """Загружаем с json цену шарнира"""
        cena = read("kalitka_kefyy.json")["price"]["sharnir"]
        sharnir_price.delete(0, last=END)
        sharnir_price.insert(0, f"{cena}")

    k_win = Tk()
    # k_win.geometry("500x500")
    k_win.title("Калитка")
    # если например в text не указать k_win то этот объект создастся в окне main2

    """Шапка"""
    width1_labl = Label(k_win, text='Большая').grid(column=1, row=1)
    width2_labl = Label(k_win, text='Меньшая').grid(column=2, row=1)
    width3_labl = Label(k_win, text='Толщина').grid(column=3, row=1)
    length1_labl = Label(k_win, text='Длина,мм').grid(column=4, row=1)
    amounttubelabl = Label(k_win, text="Кол-во")
    amounttubelabl.grid(column=5, row=1, ipadx=5, ipady=0)  # отсутпы наебашить. если ___.grid то объект возвращает нан и ipad не работает
    pricelabl = Label(k_win, text='Цена/т')
    pricelabl.grid(column=6, row=1, ipadx=11)

    """Ввод высоты и ширины"""
    text = Label(k_win, text="Введи В/Ш, мм:", width=15, anchor=E)
    text.grid(column=0, row=0, columnspan=2)
    height_kalitki = Entry(k_win, width=8)
    height_kalitki.grid(column=2, row=0)
    width_kalitki = Entry(k_win, width=8)
    width_kalitki.grid(column=3, row=0)
    fill_gen = Button(k_win, text="Заполнить", command=to_fill)
    fill_gen.grid(column=4, row=0)

    """Первый столб"""
    tube_labl = Label(k_win, text='Столбы').grid(column=0, row=2)
    width1_1 = Entry(k_win, width=8)  # Большая сторона профиля
    width1_1.insert(0, '60')
    width1_1.grid(column=1, row=2)
    width1_2 = Entry(k_win, width=8)  # Меньшая сторона профиля
    width1_2.insert(0, "60")
    width1_2.grid(column=2, row=2)
    thick1 = Entry(k_win, width=8)  # толщина профиля
    thick1.insert(0, "1.5")
    thick1.grid(column=3, row=2)
    length1 = Entry(k_win, width=8)
    # length1.insert()
    length1.grid(column=4, row=2)
    amount1 = Entry(k_win, width=8)
    amount1.insert(0, '2')
    amount1.grid(column=5, row=2)
    # amount1.insert()
    price_tube1 = Entry(k_win, width=8)
    price_tube1.insert(0, "90000")
    price_tube1.grid(column=6, row=2)

    """Второй столб"""
    width2_1 = Entry(k_win, width=8)
    #width2_1.insert(0, '60')
    width2_1.grid(column=1, row=3)
    width2_2 = Entry(k_win, width=8)
    #width2_2.insert(0, "60")
    width2_2.grid(column=2, row=3)
    thick2 = Entry(k_win, width=8)
    thick2.grid(column=3, row=3)
    length2 = Entry(k_win, width=8)
    length2.grid(column=4, row=3)
    amount2 = Entry(k_win, width=8)
    amount2.grid(column=5, row=3)
    price_tube2 = Entry(k_win, width=8)
    price_tube2.insert(0, "90000")
    price_tube2.grid(column=6, row=3, pady=5)

    """Первая рама (Два row оставлены про запас"""
    rama_labl = Label(k_win, text='Рама').grid(column=0, row=6)
    shirina_ramy1_1 = Entry(k_win, width=8)
    shirina_ramy1_1.insert(0, '60')
    shirina_ramy1_1.grid(column=1, row=6)
    shirina_ramy1_2 = Entry(k_win, width=8)
    shirina_ramy1_2.insert(0, "40")
    shirina_ramy1_2.grid(column=2, row=6)
    tolshina_ramy_1 = Entry(k_win, width=8)
    tolshina_ramy_1.insert(0, "1.5")
    tolshina_ramy_1.grid(column=3, row=6)
    dlina_ramy_1 = Entry(k_win, width=8)
    dlina_ramy_1.grid(column=4, row=6)
    amount_ramy_1 = Entry(k_win, width=8)
    amount_ramy_1.insert(0, "1")
    amount_ramy_1.grid(column=5, row=6)
    price_ramy_1 = Entry(k_win, width=8)
    price_ramy_1.insert(0, "90000")
    price_ramy_1.grid(column=6, row=6, pady=5)

    """Вторая рама"""
    shirina_ramy2_1 = Entry(k_win, width=8)
    #shirina_ramy2_1.insert(0, '60')
    shirina_ramy2_1.grid(column=1, row=7)
    shirina_ramy2_2 = Entry(k_win, width=8)
    #shirina_ramy2_2.insert(0, "40")
    shirina_ramy2_2.grid(column=2, row=7)
    tolshina_ramy_2 = Entry(k_win, width=8)
    tolshina_ramy_2.insert(0, "")
    tolshina_ramy_2.grid(column=3, row=7)
    dlina_ramy_2 = Entry(k_win, width=8)
    dlina_ramy_2.grid(column=4, row=7)
    amount_ramy_2 = Entry(k_win, width=8)
    amount_ramy_2.insert(0, "")
    amount_ramy_2.grid(column=5, row=7)
    price_ramy_2 = Entry(k_win, width=8)
    price_ramy_2.insert(0, "90000")
    price_ramy_2.grid(column=6, row=7, pady=5)

    """Фланец"""
    flanec_labl = Label(k_win, width=9, text="Фланец", anchor=W).grid(column=0, row=10)
    flanec_size = Entry(k_win, width=11)
    flanec_size.grid(column=3, row=10, columnspan=2, sticky=E, padx=6)
    flanec_amount = Entry(k_win, width=8)
    flanec_amount.grid(column=5, row=10)
    flanec_price = Entry(k_win, width=8)
    flanec_price.grid(column=6, row=10)

    """Косынки"""
    kosynka_labl = Label(k_win, width=9, text="Косынка", anchor=W).grid(column=0, row=11)
    kosynka_size = Entry(k_win, width=11)
    kosynka_size.grid(column=3, row=11, columnspan=2, sticky=E, padx=6)
    kosynka_size.insert(0, "45x55x5")
    kosynka_amount = Entry(k_win, width=8)
    kosynka_amount.grid(column=5, row=11)
    kosynka_price = Entry(k_win, width=8)
    kosynka_price.grid(column=6, row=11)

    "Шарниры"
    sharnir_labl = Label(k_win, width=9, text="Шарнир", anchor=W).grid(column=0, row=12)
    sharnir_size = Entry(k_win, width=11)
    sharnir_size.grid(column=3, row=12, columnspan=2, sticky=E, padx=6)
    sharnir_amount = Entry(k_win, width=8)
    sharnir_amount.grid(column=5, row=12)
    sharnir_amount.insert(0, "2")
    sharnir_price = Entry(k_win, width=8)
    sharnir_price.grid(column=6, row=12)

    "Заглушки"
    zagl_labl = Label(k_win, width=9, text="Заглушка", anchor=W).grid(column=0, row=13)
    zagl_size = Entry(k_win, width=11)
    zagl_size.grid(column=3, row=13, columnspan=2, padx=6, sticky=E)
    zagl_amount = Entry(k_win, width=8)
    zagl_amount.grid(column=5, row=13)
    zagl_amount.insert(0, "2")
    zagl_price = Entry(k_win, width=8)
    zagl_price.grid(column=6, row=13)

    """Панели"""
    panel_labl = Label(k_win, width=9, text="Панель", anchor=W).grid(column=0, row=14)
    panel_size = Entry(k_win, width=11)
    panel_size.grid(column=3, row=14, columnspan=2, sticky=E, padx=6)
    panel_amount = Entry(k_win, width=8)
    panel_amount.grid(column=5, row=14)
    panel_price = Entry(k_win, width=8)
    panel_price.grid(column=6, row=14)

    """Панели"""
    panel_labl2 = Label(k_win, width=9, text="Панель доб.", anchor=W).grid(column=0, row=15)
    panel_size2 = Entry(k_win, width=11)
    panel_size2.grid(column=3, row=15, columnspan=2, sticky=E, padx=6)
    panel_amount2 = Entry(k_win, width=8)
    panel_amount2.grid(column=5, row=15)
    panel_price2 = Entry(k_win, width=8)
    panel_price2.grid(column=6, row=15)

    """Уголок"""
    ug_labl = Label(k_win, width=9, text="Уголок", anchor=W).grid(column=0, row=16)
    ug_size = Entry(k_win, width=11)
    ug_size.grid(column=3, row=16, columnspan=2, sticky=E, padx=6)
    ug_amount = Entry(k_win, width=8)
    ug_amount.grid(column=5, row=16)
    ug_price = Entry(k_win, width=8)
    ug_price.grid(column=6, row=16)

    """Что-нибудь"""
    any_labl = Label(k_win, width=9, text="....", anchor=W).grid(column=0, row=17)
    any_size = Entry(k_win, width=11)
    any_size.grid(column=3, row=17, columnspan=2, sticky=E, padx=6)
    any_amount = Entry(k_win, width=8)
    any_amount.grid(column=5, row=17)
    any_price = Entry(k_win, width=8)
    any_price.grid(column=6, row=17)

    """РАЛ"""
    ral_labl = Label(k_win, text="Краска", width=9, anchor=W).grid(column=0, row=18)
    ral_price = Entry(k_win, width=8)
    ral_price.grid(column=6, row=18)

    """Вывод результата расчета"""
    summa_text = Label(k_win)
    summa_text.grid(column=6, row=21)
    summa_seb_text = Label(k_win)
    summa_seb_text.grid(column=6, row=22)
    summa_sale_text = Label(k_win)
    summa_sale_text.grid(column=6, row=23)

    """Надписи текстовые: Сумма, себестоимость, рекоменд цена"""
    summa = Label(k_win, text="Сумма", anchor=E, width=20)
    summa.grid(column=4, row=21, columnspan=2)
    summa_seb = Label(k_win, text='Себест. продукции', anchor=E, width=20)
    summa_seb.grid(column=4, row=22, columnspan=2)
    summa_sale = Label(k_win, text='Реком. цена продажи', anchor=E, width=20)
    summa_sale.grid(column=4, row=23, columnspan=2)

    """Кнопки Расчет, Детали расчета и Изменить КЭФы"""
    count_but = Button(k_win, text="Рассчитать", width=13, command=count)
    count_but.grid(column=2, columnspan=2, row=21)
    count_det_but = Button(k_win, width=13, text="Детали расчета",  command=details, state="disabled")
    count_det_but.grid(column=2, columnspan=2, row=22)
    change_kefy = Button(k_win, width=13, text="Изменить КЭФы", command=kefy)
    change_kefy.grid(column=2, columnspan=2, row=23)

    k_win.mainloop()






if __name__ == "__main__":
    create_kalitka()


"""1. 
2. acnchor работает только в паре с width=
3. Добавлять еще КЭФы к расчету
4. Добавить окно ввода плотности. Невозможно учесть все варинты профилей в БД
5. На данный момент программа работает только с профильными трубами, добавить круглые

Теперь любые ошибки в sql игнорируются, потому что я все заменяю на 0
Как к этому пришле:
 1. Ф count не может рассчитать стоимость потому что поступает:
     ValueError: invalid literal for int() with base 10: ''
2. Для лечения выставил по умолчанию в позициях значения 0 (толщина, длина, кол-во)
3. Получаю ошибку UnboundLocalError: local variable 'a' referenced before assignment т.к. line 45, in database
return a.     ----------ПОЧИНЕНО
"""
