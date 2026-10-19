import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Пример grid")

# Заголовок
tk.Label(root, text="Форма добавления", font=("Arial", 14, "bold"))\
  .grid(row=0, column=0, columnspan=2, pady=10)

# Поля ввода
tk.Label(root, text="Имя:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

# Кнопки
btn_frame = tk.Frame(root)
btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(btn_frame, text="Добавить").pack(side="left", padx=5)
tk.Button(btn_frame, text="Очистить").pack(side="left", padx=5)

# Настройка растягивания колонок
root.columnconfigure(1, weight=1)  # колонка 1 будет растягиваться

root.mainloop()