#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk


def draw_scene(canvas):
    canvas.create_rectangle(120, 150, 280, 280, fill='skyblue', outline='skyblue')
    canvas.create_polygon(100, 150, 200, 50, 300, 150, fill='skyblue', outline='skyblue')
    canvas.create_oval(350, 30, 450, 130, fill='orange', outline='orange')

    for i in range(0, 500, 20):
        canvas.create_line(i + 10, 300, i + 20, 270, fill='green', width=2)


def main():
    root = tk.Tk()
    root.title("Дом")

    canvas = tk.Canvas(root, width=500, height=300, bg='white')
    canvas.pack()

    draw_scene(canvas)

    root.mainloop()


if __name__ == "__main__":
    main()