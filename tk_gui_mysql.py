import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Работа с БД")

        # Подключение к БД
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mydb"
        )

        # Интерфейс
        self.create_widgets()

    def create_widgets(self):
        # Поля ввода
        tk.Label(self.root, text="Имя:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        # Кнопки
        tk.Button(self.root, text="Добавить",
                  command=self.add_record).grid(row=1, column=0)
        tk.Button(self.root, text="Показать все",
                  command=self.show_records).grid(row=1, column=1)

        # Таблица результатов
        self.tree = ttk.Treeview(self.root, columns=("id", "name"))
        self.tree.grid(row=2, column=0, columnspan=2)

    def add_record(self):
        name = self.name_entry.get()
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        self.db.commit()
        messagebox.showinfo("Успех", "Запись добавлена!")

    def show_records(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users")
        records = cursor.fetchall()

        # Очистка таблицы
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Заполнение данными
        for record in records:
            self.tree.insert("", "end", values=record)


if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()