#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk


class TextResizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Text Resizer")

        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=10)

        self.width_label = tk.Label(self.input_frame)
        self.width_label.grid(row=0, column=0)
        self.width_entry = tk.Entry(self.input_frame)
        self.width_entry.grid(row=0, column=1)

        self.height_label = tk.Label(self.input_frame)
        self.height_label.grid(row=1, column=0)
        self.height_entry = tk.Entry(self.input_frame)
        self.height_entry.grid(row=1, column=1)

        self.resize_button = tk.Button(self.input_frame, text="Изменить", command=self.resize_text)
        self.resize_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        self.text_area = tk.Text(master, bg="lightgrey", wrap="word")
        self.text_area.pack(padx=10, pady=10)

        self.text_area.bind("<FocusIn>", self.on_focus_in)
        self.text_area.bind("<FocusOut>", self.on_focus_out)

        master.bind("<Return>", self.resize_text)

    def resize_text(self, event=None):
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            self.text_area.config(width=width, height=height)
        except ValueError:
            pass

    def on_focus_in(self, event):
        self.text_area.config(bg="white")

    def on_focus_out(self, event):
        self.text_area.config(bg="lightgrey")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextResizerApp(root)
    root.mainloop()