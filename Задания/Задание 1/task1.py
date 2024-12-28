#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import messagebox


class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping List")

        self.items = ["apple", "bananas", "carrot", "bread", "butter", 
                      "meat", "potato", "pineapple", "tomato", "milk"]

        # Создаем рамки для списка доступных товаров и списка покупок
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.available_listbox = tk.Listbox(self.frame, selectmode=tk.MULTIPLE, width=30, height=10)
        self.available_listbox.pack(side=tk.LEFT, padx=(0, 10))

        for item in self.items:
            self.available_listbox.insert(tk.END, item)

        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.button_frame, text=">>>", command=self.add_to_shopping_list)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.button_frame, text="<<<", command=self.remove_from_shopping_list)
        self.remove_button.pack(pady=5)

        self.shopping_listbox = tk.Listbox(self.frame, selectmode=tk.MULTIPLE, width=30, height=10)
        self.shopping_listbox.pack(side=tk.LEFT, padx=(10, 0))

    def add_to_shopping_list(self):
        selected_items = self.available_listbox.curselection()
        if not selected_items:
            messagebox.showwarning("Предупреждение", "Выберите хотя бы один товар для добавления.")
            return

        for index in selected_items[::-1]:
            item = self.available_listbox.get(index)
            self.shopping_listbox.insert(tk.END, item)
            self.available_listbox.delete(index)

    def remove_from_shopping_list(self):
        selected_items = self.shopping_listbox.curselection()
        if not selected_items:
            messagebox.showwarning("Предупреждение", "Выберите хотя бы один товар для удаления.")
            return

        for index in selected_items[::-1]:
            item = self.shopping_listbox.get(index)
            self.available_listbox.insert(tk.END, item)
            self.shopping_listbox.delete(index)


if __name__ == '__main__':
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()