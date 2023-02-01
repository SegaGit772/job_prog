import tkinter as tk

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Это всплывающее окно")
        self.button = tk.Button(self, text="Закрыть", command=self.destroy)

        self.label.pack(padx=20, pady=20)
        self.button.pack(pady=5, ipadx=2, ipady=2)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self, text="Открыть новое окно",
                             command=self.open_window)
        self.btn.pack(padx=50, pady=20)

    def open_window(self):
        about = About(self)
        about.grab_set()

if __name__ == "__main__":
    app = App()
    app.mainloop()