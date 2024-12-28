#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import Listbox, Scrollbar, END


class TextListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Listbox Example")

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.entry.bind('<Return>', self.add_text)

        self.listbox = Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.listbox.bind('<Double-Button-1>', self.copy_to_entry)

    def add_text(self, event):
        text = self.entry.get()
        if text: 
            self.listbox.insert(END, text)
            self.entry.delete(0, END)

    def copy_to_entry(self, event):
        try:
            selected_index = self.listbox.curselection()[0]
            selected_text = self.listbox.get(selected_index)
            self.entry.delete(0, END)
            self.entry.insert(0, selected_text)
        except IndexError:
            pass


if __name__ == '__main__':
    root = tk.Tk()
    app = TextListApp(root)
    root.mainloop()