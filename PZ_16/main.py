import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#c7897d', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="test/BD/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить клиента', command=self.open_dialog, bg='#c7897d', bd=0, fg='white',
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.edit_img = tk.PhotoImage(file="test/BD/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#c7897d',
                                    bd=0, fg='white', compound=tk.TOP, image=self.edit_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="test/BD/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#c7897d',
                               bd=0, fg='white', compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="test/BD/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#c7897d',
                               bd=0, fg='white', compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="test/BD/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#c7897d',
                                bd=0, fg='white', compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'name', 'payment',
                                                'percent', 'time_expection', 'b_card', 'summary'), height=15, show='headings')

        self.tree.column('user_id', width=75, anchor=tk.CENTER)
        self.tree.column('name', width=180, anchor=tk.CENTER)
        self.tree.column('payment', width=140, anchor=tk.CENTER)
        self.tree.column('percent', width=140, anchor=tk.CENTER)
        self.tree.column('time_expection', width=140, anchor=tk.CENTER)
        self.tree.column('b_card', width=140, anchor=tk.CENTER)
        self.tree.column('summary', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='Код клиента')
        self.tree.heading('name', text='Ф.И.О.')
        self.tree.heading('payment', text='Периодический платеж')
        self.tree.heading('percent', text='Годовой %')
        self.tree.heading('time_expection', text='Срок вклада')
        self.tree.heading('b_card', text='Пластиковая карта')
        self.tree.heading('summary', text='Конечная сумма')

        self.tree.pack()

    def records(self, user_id, name, payment, percent, time_expection, b_card, summary):
        self.db.insert_data(user_id, name, payment, percent, time_expection, b_card, summary)
        self.view_records()

    def update_record(self, user_id, name, payment, percent, time_expection, b_card, summary):
        self.db.cur.execute(
            """UPDATE users SET user_id=?, name=?, payment=?, percent=?, time_expection=?, b_card=?, summary=? WHERE user_id=?""",
            (user_id, name, payment, percent, time_expection, b_card, summary, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE user_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, name):
        name = (name + " %",)
        print(name)
        self.db.cur.execute("SELECT * FROM users WHERE name LIKE ?", name)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить клиента')
        self.geometry('400x300+400+300')
        self.resizable(False, False)
        label_description = tk.Label(self, text='Код клиента')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=225, y=25)
        label_name = tk.Label(self, text='Ф.И.О.')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=225, y=50)
        label_payment = tk.Label(self, text='Периодический платеж')
        label_payment.place(x=50, y=75)
        self.entry_payment = ttk.Entry(self)
        self.entry_payment.place(x=225, y=75)
        #self.combobox = ttk.Combobox(self, values=[u'Мужской', u'Женский'])
        #self.combobox.current(0)
        #self.combobox.place(x=110, y=75)
        label_perc = tk.Label(self, text='Процент')
        label_perc.place(x=50, y=100)
        self.entry_perc = ttk.Entry(self)
        self.entry_perc.place(x=225, y=100)
        label_time = tk.Label(self, text='Срок вклада')
        label_time.place(x=50, y=125)
        self.entry_time = ttk.Entry(self)
        self.entry_time.place(x=225, y=125)
        label_card = tk.Label(self, text='Пластиковая карта')
        label_card.place(x=50, y=150)
        self.combobox = ttk.Combobox(self, values=[u'Да', u'Нет'])
        self.combobox.current(0)
        self.combobox.place(x=225, y=150)
        label_summary = tk.Label(self, text='Конечная сумма')
        label_summary.place(x=50, y=175)
        self.entry_summary = ttk.Entry(self)
        self.entry_summary.place(x=225, y=175)
        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=250)
        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=250)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_payment.get(),
                                                                       self.entry_perc.get(),
                                                                       self.entry_time.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_summary.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=200, y=250)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_payment.get(),
                                                                          self.entry_perc.get(),
                                                                          self.entry_time.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_summary.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")

        self.geometry("300x100+400+300")
        self.resizable(False, False)
        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)
        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)
        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)
        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event:
        self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('test/BD/bank.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                payment INTEGER,
                percent REAL,
                time_expection TEXT,
                b_card TEXT,
                summary INTEGER
            )""")

    def insert_data(self, user_id, name, payment, percent, time_expection, b_card, summary):
        self.cur.execute("""INSERT INTO users(user_id, name, payment, percent, time_expection, b_card, summary) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
                         (user_id, name, payment, percent, time_expection, b_card, summary))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("База данных ")
    root.geometry("950x450+300+200")
    root.resizable(False, False)
    root.mainloop()